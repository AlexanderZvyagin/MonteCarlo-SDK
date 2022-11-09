import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
from mcsdk import *
server = 'http://localhost:8080'
#server = 'http://naz.hopto.org:8001'
