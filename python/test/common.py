import requests
from server import server
import mcsdk as sdk

HttpStatusOK = 200

def run(model:sdk.Model) -> sdk.EvaluationResults:
    response = requests.post(f'{server()}/model',sdk.Model_to_json_string(model))
    assert response.status_code == HttpStatusOK
    er = sdk.EvaluationResults_from_json_string(response.text)
    er.model = model
    return er
