
class Config(object):
    SECRET_KEY = 'NbAbBqRBv0I'


def TestConfig(Config):
    TESTING =True
    DEBUG =True

def ProdConfig(Config):
    DEBUG =False
    TESTING = False

def DevConfig(Config):
    DEBUG = True

app_config = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing' : TestConfig
}