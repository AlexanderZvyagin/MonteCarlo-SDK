import requests, json, logging
logging.basicConfig (
    format = '%(asctime)s [%(levelname)s] %(message)s',
    level = logging.INFO
)
from mcsdk import *
import mcsdk.examples
server = 'http://localhost:8080'

def linspace(min:float,max:float,n:int):
    assert n>=2 and min!=max
    step = (max-min)/n
    return [min] + [min+step*i for i in range(1,n-2)] + [max]
