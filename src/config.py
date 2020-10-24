import os


DEFAULT_BIND_PORT = 8800
DEFAULT_BIND_HOST = "127.0.0.1"

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'booginmcbaggins'
