"""Flask config class."""
import pathlib
from os.path import dirname, abspath, join


class Config(object):
    """Set Flask base configuration"""
    SECRET_KEY = 'scrtkwy' # Replace with your own secret key! This should not be visible to others.
    WTF_CSRF_SECRET_KEY = 'a4OsmvYQzG3oC_pwM_e3yA'

class ProdConfig(Config):
    ENV = 'production' # Warning: this is not the recommended method but should suffice for our app
    DEBUG = False
    TESTING = False


class TestConfig(Config):

    ENV = 'testing'
    DEBUG = False
    TESTING = True
    SQLALCHEMY_ECHO = True


class DevConfig(Config):

    ENV = 'development'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = True
