import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
import mcsdk as sdk
server = 'http://naz.hopto.org:8001'
