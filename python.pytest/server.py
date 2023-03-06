import os

def server():
    address = os.environ['SERVER_ADDRESS']
    port    = int(os.environ['SERVER_PORT'])
    return f'http://{address}:{port}'
