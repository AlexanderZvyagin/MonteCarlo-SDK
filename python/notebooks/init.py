import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
import mcsdk as sdk
server = 'http://naz.hopto.org:8001'

class McSdkException(Exception):
    def __init__ (self,error:sdk.Error):
        super().__init__(error.message)
        self.error = error
    
def run(model:sdk.Model) -> sdk.EvaluationResults:
    response = requests.post(f'{server}/model',sdk.Model_to_json_string(model))
    if response.status_code == 200:
        result = sdk.EvaluationResults_from_json_string(response.text)
        result.model = model
        return result
    else:
        error = sdk.Error_from_json_string(response.text)
        raise McSdkException (error)
