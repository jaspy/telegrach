from mongoengine import connect
from . import config
import os


class Config:

    @classmethod
    def init_app(cls, app):
        cls.connection()


class DevelopmentConfig(Config):
    DEBUG = True
    os.environ['FLASK_CONFIG'] = 'development'
    os.environ['FLASK_ENV'] = 'development'

    @staticmethod
    def connection():
        connect(
            db=config.mongodb['db'],
            username=config.mongodb['username'],
            password=config.mongodb['password'],
            host=config.mongodb['host'],
            port=config.mongodb['port'],
        )


class TestingConfig(Config):
    TESTING = True

    @staticmethod
    def connection():
        connect(
            db=config.mongodb_test['db'],
            username=config.mongodb_test['username'],
            password=config.mongodb_test['password'],
            host=config.mongodb_test['host'],
            port=config.mongodb_test['port'],
        )


# class ProductionConfig(Config):
#     pass


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}