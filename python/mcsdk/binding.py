import json
import math
import pandas as pd

class Parameter:
    def __init__ (self,name,value=None,step=None,min=None,max=None):
        self.name = name
        if value is not None: self.value = value
        if step is not None: self.step = step
        if min is not None: self.min = min
        if max is not None: self.max = max
    def json (self):
        return json.dumps(self,default=vars)

class EvaluationPoint:
    def __init__ (self,state,time,value=None,error=None):
        self.state = state
        self.time = time
        if value is not None: self.value = value
        if error is not None: self.error = error
    def json (self):
        return json.dumps(self,default=vars)

class Updater:
    def __init__ (self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
    # def __init__ (self,type,name='',start=None,args=[],refs=[]):
    #     self.type = type
    #     self.name = name
    #     self.start = start
    #     self.args = args
    #     self.refs = refs
    def json (self):
        return json.dumps(self,default=vars)

class Model:
    def __init__ (self):
        self.TimeStart = 0
        self.TimeSteps = 1
        self.NumPaths = 1
        self.updaters = []
        self.evaluations = []
    def NumStatefulProcesses (self):
        return len([x for x in self.updaters if hasattr(x,'start')])
    def json (self):
        return json.dumps(self,default=vars)

class Result:
    def __init__ (self,n=0,mean=None,stddev=None,skewness=None):
        self.n = n
        self.mean = mean
        self.stddev = stddev
        self.skewness = skewness
    def MeanError (self):
        return None if self.stddev is None else self.stddev/math.sqrt(self.n)
    def __str__ (self):
        return f'n={self.n} mean={self.mean} +/- {self.MeanError()}'
    def __repr__ (self):
        return str(self)
    
class EvaluationResults:
    def __init__ (self,data,model=None):
        self.model = model
        self.names = data['names']
        self.npaths = data['npaths']
        self.mean = data['mean']
        self.stddev = data['stddev']
        self.skewness = data['skewness']
        self.time_points = data['time_points']
        self.time_steps = data['time_steps']
        
        self.Validation ()
        
    def Validation (self):
        assert self.model is not None
        assert len(self.time_points) == len(self.time_steps)
        n = self.NumStates()*self.NumEvaluations()
        assert n == len(self.npaths)
        assert n == len(self.mean)
        assert n == len(self.stddev)
        assert n == len(self.skewness)
        
    def NumStates (self):
        return len(self.names)
    def NumEvaluations (self):
        return len(self.time_points)
    
    def Index (self,state,point):
        assert state>=0 and state<self.NumStates()
        assert point>=0 and point<self.NumEvaluations()
        return point*self.NumStates() + state
    
    def GetStateEvaluationResult (self,state,point):
        n = self.Index(state,point)
        return Result(self.npaths[n],self.mean[n],self.stddev[n],self.skewness[n])
    
    def df (self):
        data = []
        for j in range(self.NumEvaluations()):
            for i in range(self.NumStates()):
                n = self.Index(i,j)
                data.append({
                    'name': self.names[i],
                    'state': i,
                    'time': self.time_points[j],
                    'step': self.time_steps[j],
                    'npaths': self.npaths[n],
                    'mean':self.mean[n],
                    'mean_error': None if self.stddev[n] is None else self.stddev[n]/math.sqrt(self.npaths[n]),
                    'stddev': self.stddev[n],
                    'skewness': self.skewness[n]
                })
        return pd.DataFrame(data)
    def __str__ (self):
        return f'{self.NumStates()} states with {self.NumEvaluations()} evaluations'
    def __repr__ (self):
        return str(self)