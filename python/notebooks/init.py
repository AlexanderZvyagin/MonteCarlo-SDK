import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
import mcsdk as sdk
server = 'http://naz.hopto.org:8001'

def run(model:sdk.Model) -> sdk.EvaluationResults:
    response = requests.post(f'{server}/model',sdk.Model_to_json_string(model))
    assert response.status_code == 200
    er = sdk.EvaluationResults_from_json_string(response.text)
    er.model = model
    return er