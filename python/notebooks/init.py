import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
import mcsdk as sdk
from plot import *
import os
server = os.getenv("SERVER_ADDRESS")
if not server:
    raise Exception('Please, set SERVER_ADDRESS environment variable, e.g. SERVER_ADDRESS=http://my.host:port/addr')
