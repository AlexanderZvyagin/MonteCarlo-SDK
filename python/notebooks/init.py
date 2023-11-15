import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
import mcsdk as sdk
from plot import plot
import os
server = f'http://{os.getenv("SERVER_ADDRESS","naz.hopto.org")}:{os.getenv("SERVER_PORT","8001")}'
