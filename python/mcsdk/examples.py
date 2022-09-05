from .binding import *

def BuildModel_Simple ():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.updaters.append(Updater(
        name = "IndependentBrownianMotion"
    ))
    m.updaters.append(Updater(
        name = "BrownianMotion",
        start = 0.1,
        args = [0.2,2] # drft, diffusion
    ))
    return m

def TwoProcessesModel ():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.updaters.append(Updater(
        name = "IndependentBrownianMotion"
    ))
    m.updaters.append(Updater(
        name = "BrownianMotion",
        start = 0.1,
        args = [0.2,2] # drft, diffusion
    ))
    m.updaters.append(Updater(
        name = "BrownianMotion",
        start = 0.1,
        args = [0.2,2] # drft, diffusion
    ))
    return m