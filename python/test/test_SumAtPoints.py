from common import *

def test_server_available():
    assert server()

    for endpoint in ('/','/functions','/metrics'):
        response = requests.get(f'{server()}{endpoint}')
        assert response.status_code==200

def test_simple_model():
    model = sdk.Model()

    model.TimeStart = 0
    model.TimeSteps = 10
    model.NumPaths = 1
    model.Add(sdk.IndependentGaussian())
    model.Add(sdk.BrownianMotion(0.1,0.2,2)) # start, drift, diffusion

    model.evaluations.append(sdk.EvaluationPoint(0,2))

    er = run(model)
    assert len(er.names)==1
