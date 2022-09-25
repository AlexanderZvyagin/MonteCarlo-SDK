import json
import math
import pandas as pd
from enum import IntEnum
from typing import List

# class Parameter:
#     def __init__ (self,value=None,step=None,min=None,max=None):
#         if value is not None: self.value = value
#         if step is not None: self.step = step
#         if min is not None: self.min = min
#         if max is not None: self.max = max
#     def json (self):
#         return json.dumps(self,default=vars)

class HistogramAxis:
    def __init__ (self, state, bins, min, max):
        self.state = state
        self.bins = bins
        self.min = min
        self.max = max
    def json (self):
        return json.dumps(self,default=vars)

class Histogram:
    def __init__ (self, x:HistogramAxis, y=None):
        self.x = x
        if y: self.y = y
    def json (self):
        return json.dumps(self,default=vars)

class EvaluationPoint:
    def __init__ (self,state:int,time:float,value:float=None,error:float=None):
        self.state = state
        self.time = time
        if value is not None: self.value = value
        if error is not None: self.error = error
        self.histograms = []
    def Add (self,histogram):
        self.histograms.append(histogram)
        return self
    def json (self):
        return json.dumps(self,default=vars)

class Updater:
    def __init__ (self,**kwargs):
        for k,v in kwargs.items():
            # assert k in ['name','args','refs','start']
            setattr(self,k,v)
    def Number (self):
        return self._eq
    def json (self):
        return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class IndependentBrownianMotion (Updater):
    def __init__ (self):
        Updater.__init__ (
            self,
            name  = 'IndependentBrownianMotion'
        )

class BrownianMotion (Updater):
    def __init__ (self, start:float, drift:float, diffusion:float, title:str=''):
        Updater.__init__ (
            self,
            name  = 'BrownianMotion',
            start = start,
            args  = [drift,diffusion],
            _title = title
        )

class BrownianMotionRef (Updater):
    def __init__ (self, start:float, drift:int, diffusion:int, title:str=''):
        Updater.__init__ (
            self,
            name  = 'BrownianMotion',
            start = start,
            refs  = [drift,diffusion],
            _title = title
        )

class GeometricalBrownianMotion (Updater):
    def __init__ (self, start:float, drift:float, diffusion:float, title:str=''):
        Updater.__init__ (
            self,
            name  = 'GeometricalBrownianMotion',
            start = start,
            args  = [drift,diffusion],
            _title = title
        )

class GeometricalBrownianMotionRef (Updater):
    def __init__ (self, start:float, drift:int, diffusion:int, title:str=''):
        Updater.__init__ (
            self,
            name  = 'GeometricalBrownianMotion',
            start = start,
            args  = [drift,diffusion],
            _title = title
        )

class Product_Option (Updater):
    Call = 0
    Put = 1
    def __init__ (self, underlying:int, strike:float, call_put:int, title:str=''):
        Updater.__init__ (
            self,
            name  = 'Product_Option',
            start = None,
            refs = [underlying],
            args = [strike,call_put],
            _title = title
        )

class Barrier (Updater):
    class Direction (IntEnum):
        Up   = 1
        Down = -1
        Any  = 0
    class Action (IntEnum):
        Set = 0
    def __init__ (self, underlying:int, start:float, level:float, value:float, direction:Direction, action:Action, title:str=''):
        Updater.__init__ (
            self,
            name  = 'Barrier',
            start = start,
            refs = [underlying],
            args = [level, value, direction, action],
            _title = title
        )

class Multiplication (Updater):
    def __init__ (self, start:float, refs:List[int], title:str=''):
        Updater.__init__ (
            self,
            name  = 'Multiplication',
            start = start,
            refs = refs,
            _title = title
        )

class Model:
    def __init__ (self):
        self.TimeStart = 0
        self.TimeSteps = 1
        self.NumPaths = 1
        self.updaters = []
        self.evaluations = []
        self.RandomSeed = -1 # generate random seed
        self._titles = {}
    def Add (self, updater: Updater):
        self.updaters.append(updater)
        title = getattr(updater,'_title',None)
        updater._eq = self.NumStatefulProcesses()-1
        self._titles[updater._eq] = title
    def NumStatefulProcesses (self):
        return len([x for x in self.updaters if hasattr(x,'start')])
    def json (self):
        return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

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
        error = data.get('error')
        if error:
            raise Exception(error)
        self.names = data['names']
        self.npaths = data['npaths']
        self.mean = data['mean']
        self.stddev = data['stddev']
        self.skewness = data['skewness']
        self.time_points = data['time_points']
        self.time_steps = data['time_steps']
        self.histograms = data['histograms']
        self.model = model
        
        self.Validation ()
        
    def Validation (self):
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
                item = {
                    'name': self.names[i],
                    'title': '',
                    'state': i,
                    'time': self.time_points[j],
                    'step': self.time_steps[j],
                    'npaths': self.npaths[n],
                    'mean':self.mean[n],
                    'mean_error': None if self.stddev[n] is None else self.stddev[n]/math.sqrt(self.npaths[n]),
                    'stddev': self.stddev[n],
                    'skewness': self.skewness[n]
                }
                if self.model:
                    item['title'] = self.model._titles.get(i,'')
                data.append(item)
        return pd.DataFrame(data)
    def __str__ (self):
        return f'{self.NumStates()} states with {self.NumEvaluations()} evaluations'
    def __repr__ (self):
        return str(self)
