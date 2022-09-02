import json

class Parameter:
    def __init__ (self,name='',value=None,step=None,min=None,max=None):
        if name: self.name = name
        if value is not None: self.value = value
        if step is not None: self.step = step
        if min is not None: self.min = min
        if max is not None: self.max = max
    def toJson (self):
        return json.dumps(self,default=vars)

class EvaluationPoint:
    def __init__ (self,state,time,value=None,error=None):
        self.state = state
        self.time = time
        if value is not None: self.value = value
        if error is not None: self.error = error
    def toJson (self):
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
    def toJson (self):
        return json.dumps(self,default=vars)

class Model:
    def __init__ (self):
        self.TimeStart = 0
        self.TimeSteps = 1
        self.NumPaths = 1
        self.updaters = []
        self.evaluations = []
    def toJson (self):
        return json.dumps(self,default=vars)
