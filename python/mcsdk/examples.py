from .binding import *

def BuildModel_Simple ():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.updaters.append(Updater(
        type = "IndependentBrownianMotion",
        name = "IndependentBrownianMotion"
    ))
    m.updaters.append(Updater(
        type = "SimpleBrownianMotion",
        name = "SimpleBrownianMotion",
        start = Parameter("start",0.1),
        args = [
            Parameter("drift",0.2),
            Parameter("diffusion",2)
        ]
    ))
    return m

def BadModel ():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.updaters.append(Updater(
        type = "Error",
        name = "Error"
    ))
    return m
