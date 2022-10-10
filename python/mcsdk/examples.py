from .dto import *

def BuildModel_Simple ():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.Add(IndependentGaussian())
    m.Add(BrownianMotion(0.1,0.2,2)) # start, drift, diffusion
    return m

def TwoProcessesModel ():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.Add(IndependentGaussian())
    m.Add(BrownianMotion(0.1,0.2,2)) # start, drift, diffusion
    m.Add(BrownianMotion(0.1,0.2,2)) # start, drift, diffusion
    return m