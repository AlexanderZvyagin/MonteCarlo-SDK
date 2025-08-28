from .dto import *

def SimpleBrownianMotionModel():
    m = Model()
    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 100
    m.Add(BrownianMotion(0.1,0.2,2)) # start, drift, diffusion
    return m

def test(server='https://mc0.netlify.app/engine-8200'):

    model = SimpleBrownianMotionModel()
    for t in [1,2]:
        model.evaluations.append(EvaluationPoint(t))
    results = run (model, server)
    return results.df()
