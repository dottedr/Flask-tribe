import os

class Config:
    """
    Base configuration class for app-wide settings. 
    Returns default configurations 
    """
    # keep debug false to avoid debug logs leaking, if this config set ends up in prod
    DEBUG = False

    # secret that is the same for each env
    SOME_SECRET = os.environ['SOME_SECRET']


class TestConfig(Config):
    DEBUG = True
    DB_SECRET = os.environ['TEST_DB_SECRET']


class ProdConfig(Config):
    DEBUG = False
    DB_SECRET = os.environ['PROD_DB_SECRET']


class DevConfig(Config):
    DEBUG = True
    DB_SECRET = os.environ['DEV_DB_SECRET']