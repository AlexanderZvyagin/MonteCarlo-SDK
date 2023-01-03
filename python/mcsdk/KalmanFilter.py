import numpy as np

def CreateMatrix (rows, cols, value=0):
    return np.matrix([[value]*cols]*rows, dtype=np.float64)

class UnscentedKalmanFilter:
    
    def __init__ (self):
        self.L = 0
        self.M = 0
        self.alpha = 0.5
        self.beta  = 2
    
    def Init (self, L, M):
        assert L>0 and M>0
        assert self.L==0 and self.M==0
        self.L = L
        self.M = M
        self.kappa = 3-L
        self._lambda = self.alpha**2 * (self.L+self.kappa) - self.L;
        w = 1.0/(2*(self.L+self._lambda))

        self.Wm = [w] * (2*self.L+1)
        self.Wc = [w] * (2*self.L+1)
        
        self.Wm[0] = self._lambda / (self.L+self._lambda)
        self.Wc[0] = self.Wm[0] + (1 - self.alpha**2 + self.beta)
        
    def RunAllIterations (self, iteration_start:int, iteration_last:int):
        iteration = iteration_start
        while iteration<=iteration_last:
            self.RunSingleIteration (iteration)
            iteration += 1
        
    def RunSingleIteration (self, iteration):
        assert self.x.shape == (self.L,1)
        assert self.P.shape == (self.L,self.L)
        
        sigma_points_generated = self.GenerateSigmaPoints()
        
        sigma_points_predicted = self.PropogateSigmaPoints(sigma_points_generated, iteration)
        
        self.Log (iteration, 'predicted sigma points', sigma_points_predicted)
        
        # Eq (12)
        predicted_state_estimate = CreateMatrix(self.L,1)
        for i in range(self.L*2+1):
            predicted_state_estimate += self.Wm[i] * sigma_points_predicted[i]

        self.Log (iteration, 'predicted state estimate', predicted_state_estimate)
        
        # Eq (13)
        diff_predicted_sigma_points = []
        error_cov = CreateMatrix(self.L,self.L)
        for i in range(self.L*2+1):
            diff = sigma_points_predicted[i] - predicted_state_estimate
            diff_predicted_sigma_points.append(diff)
            error_cov += self.Wc[i] * diff * diff.getT()
        
        self.Log (iteration, 'predicted error cov', error_cov)
        
        # Eq (14)
        predicted_measurement  = CreateMatrix(self.M,1)
        predicted_measurements_for_sigma_points = []
        for i in range(self.L*2+1):
            measurement = self.GetPredictedMeasurement (sigma_points_predicted[i], iteration)
            predicted_measurements_for_sigma_points.append(measurement)
            predicted_measurement += self.Wm[i] * measurement
        
        self.Log(iteration, 'predicted_measurement:', predicted_measurement)
        
        # Eq (15), Eq (16)
        
        measurement_tuple = self.GetMeasurement (iteration)
        self.Log (iteration, 'actual measurement', measurement_tuple)
        measurement_value = measurement_tuple[0]
        measurement_error = measurement_tuple[1]
        
        predicted_covariance = CreateMatrix(self.M, self.M)
        predicted_covariance += measurement_error
        cross_predicted_covariance = CreateMatrix (self.L, self.M)
        
        diff_measurements = []
        for i in range(self.L*2+1):
            diff = predicted_measurements_for_sigma_points[i] - predicted_measurement
            diff_measurements.append(diff)
            predicted_covariance += self.Wc[i] * diff * diff.getT()
            cross_predicted_covariance += self.Wc[i] * diff_predicted_sigma_points[i] * diff.transpose()
        
        # Eq (17)
        residual = predicted_measurement - measurement_value
        self.Log (iteration, 'residual', residual)

        # Eq (18)
        kalman_gain = cross_predicted_covariance * predicted_covariance.getI()
        self.Log (iteration, 'kalman_gain', kalman_gain)
        
        updated_state_estimate = predicted_state_estimate - kalman_gain * residual
        
        updated_cov_matrix = error_cov - kalman_gain * predicted_covariance * kalman_gain.getT()

#         if debug:
#             PrintThis([error_cov],f'iteration {iteration} old error_cov')
#             PrintThis([kalman_gain * predicted_covariance * kalman_gain.getT()],f'iteration {iteration} K*Innovations*Ktransposed')

        self.x = updated_state_estimate
        self.P = updated_cov_matrix
        
        self.Log (iteration, 'new state and its error matrix', [self.x, self.P])
        
    def GenerateSigmaPoints (self):
        '''This is a const method'''
        
        sigma_points = [self.x]

        Psqrt = np.linalg.cholesky(self.P) * np.sqrt(self.L+self._lambda)

        for i in range(self.L):
            sigma_points.append(self.x+Psqrt[:,i])
        for i in range(self.L):
            sigma_points.append(self.x-Psqrt[:,i])

        return sigma_points
        
    def PropogateSigmaPoints (self, sigma_points, iteration, debug=0):
        '''Propogate sigma points (from one iteration to another)
        
        We don't modify sigma points anything by default.
        
        This is a const method
        '''
        return sigma_points
        
    def GetPredictedMeasurement (self, state, iteration):
        raise NotImplementedError('This method must be implemented in a derived class.')
        
    def GetMeasurement (self, iteration):
        raise NotImplementedError('This method must be implemented in a derived class.')
        
    def Log (self, iteration, name, value):
        pass

class KalmanFilterMonitor:

    def __init__ (self, kf):
        self._kf = kf
        self._data = []

    def AddData (self, iteration, name, value):

        data = None
        for row in self._data:
            if row['iteration'] == iteration:
                data = row
                break
        if data is None:
            data = {'iteration':iteration}
            self._data.append(data)
        
        L = self._kf.L
        M = self._kf.M
        
        if hasattr(self._kf,'GetMeasurementGramMatrix'):
            measurement_gram_matrix = self._kf.GetMeasurementGramMatrix()
            assert gram_matrix.shape == (M,M)
        else:
            measurement_gram_matrix = CreateMatrix(M,M)
            for i in range(M):
                measurement_gram_matrix[i,i] = 1
        
        if hasattr(self._kf,'GetStateGramMatrix'):
            state_gram_matrix = self._kf.GetStateGramMatrix()
            assert gram_matrix.shape == (L,L)
        else:
            state_gram_matrix = CreateMatrix(L,L)
            for i in range(L):
                state_gram_matrix[i,i] = 1
        
        match name:
            case 'residual':
                for i in range(M):
                    data[f'residual[{i}]'] = value[i,0]
                length = (value.getT()*measurement_gram_matrix*value)
                assert length.shape == (1,1)
                data[f'residual.length'] = length[0,0]
            case 'new state and its error matrix':
                state = value[0]
                for i in range(L):
                    data[f'state[{i}]'] = state[i,0]
                if hasattr(self._kf,'GetTrueState'):
                    state_diff = state - self._kf.GetTrueState()
                    for i in range(L):
                        data[f'state_diff[{i}]'] = state_diff[i,0]
                    length = (state_diff.getT()*state_gram_matrix*state_diff)
                    assert length.shape == (1,1)
                    data[f'state_diff.length'] = length[0,0]
#             case _:
#                 print(f'unmatched {name}')
        