from mongoengine import connect
import os
from subprocess import call

class Config:
    @classmethod
    def init_app(cls, app):
        cls.connection()


class DevelopmentConfig(Config):
    DEBUG = True

    @staticmethod
    def connection():
        connect(
            db=str(os.getenv("FLASK_MONGODB_DBNAME")),
            username=str(os.getenv("FLASK_MONGODB_USERNAME")),
            password=str(os.getenv("FLASK_MONGODB_USERPASSWORD")),
            host=str(os.getenv("FLASK_MONGODB_HOST")),
            port=int(os.getenv("FLASK_MONGODB_PORT")),
        )


class TestingConfig(Config):
    TESTING = True

    @staticmethod
    def connection():
        connect(
            db=os.getenv("FLASK_MONGODB_DBNAME"),
            username=os.getenv("FLASK_MONGODB_USERNAME"),
            password=os.getenv("FLASK_MONGODB_USERPASSWORD"),
            host=os.getenv("FLASK_MONGODB_HOST"),
            port=int(os.getenv("FLASK_MONGODB_PORT")),
        )


class ProductionConfig(Config):
    @staticmethod
    def connection():
        connect(
            db=os.getenv("FLASK_MONGODB_DBNAME"),
            username=os.getenv("FLASK_MONGODB_USERNAME"),
            password=os.getenv("FLASK_MONGODB_USERPASSWORD"),
            host=os.getenv("FLASK_MONGODB_HOST"),
            port=int(os.getenv("FLASK_MONGODB_PORT")),
        )


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}