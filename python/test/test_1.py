import os, requests
import mcsdk as sdk
from init import server

def test_server_available():
    for endpoint in ('/','/functions','/metrics'):
        response = requests.get(f'{server}{endpoint}')
        assert response.status_code==200

def BuildModel_Simple():
    m = sdk.Model()

    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.Add(sdk.BrownianMotion(0.1,0.2,2)) # start, drift, diffusion

    m.evaluations.append(sdk.EvaluationPoint(2))

    return m

def test_simple_model():
    er = sdk.run( BuildModel_Simple(), server )
    print(er)
    assert len(er.names)==1

def test_functions_endpoint():
    response = requests.get(f'{server}/functions').json()
    for j in response:
        f = sdk.UpdaterDoc()
        sdk.UpdaterDoc_to_json(j,f)
