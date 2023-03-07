from server import server
import requests

def test_server_available():
    assert server()

    for endpoint in ('/','/functions','/metrics'):
        response = requests.get(f'{server()}{endpoint}')
        assert response.status_code==200
