import requests

from server import server
import mcsdk as sdk

HttpStatusOK = 200

def test_server_available():
    assert server()

    for endpoint in ('/','/functions','/metrics'):
        response = requests.get(f'{server()}{endpoint}')
        assert response.status_code==200

def BuildModel_Simple():
    m = sdk.Model()

    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.Add(sdk.IndependentGaussian())
    m.Add(sdk.BrownianMotion(0.1,0.2,2)) # start, drift, diffusion

    m.evaluations.append(sdk.EvaluationPoint(0,2))

    return m

def run(model:sdk.Model) -> sdk.EvaluationResults:
    response = requests.post(f'{server()}/model',sdk.Model_to_json_string(model))
    assert response.status_code == HttpStatusOK
    er = sdk.EvaluationResults_from_json_string(response.text)
    er.model = model
    return er

def test_simple_model():
    er = run( BuildModel_Simple() )
    print(er)
    assert len(er.names)==1
