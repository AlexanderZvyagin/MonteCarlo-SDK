import requests

class SdkException (Exception):
    def __init__ (self,error:Error):
        super().__init__(error.message)
        self.error = error
    def __str__ (self):
        return f'{self.message}'
    
def run (model:Model, server:str) -> EvaluationResults:
    response = requests.post(f'{server}/model',Model_to_json_string(model))
    if response.status_code == 200:
        result = EvaluationResults_from_json_string(response.text)
        result.model = model
        return result
    else:
        error = Error_from_json_string(response.text)
        raise SdkException (error)
