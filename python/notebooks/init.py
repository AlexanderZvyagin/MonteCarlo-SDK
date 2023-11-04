import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
import mcsdk as sdk
import os
server = f'http://{os.getenv("SERVER_ADDRESS","az.hopto.org")}:{os.getenv("SERVER_PORT","8001")}'
