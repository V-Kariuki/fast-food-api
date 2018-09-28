import os

'''class Config(object):
    """ Parent configuration class """
    pass
    
'''
class DevelopmentConfig():
    """ Development configuration class that inherits from the Config Parent Class"""
    DEBUG = True

class TestConfig():
    """ Testing configuration class that inherits from the Config Parent Class"""
    DEBUG = True
    TESTING = True

class ProductionConfig():
    """ Prduction configuration class that inherits from the Config Parent Class"""
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig
}