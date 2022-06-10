import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True