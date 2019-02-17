from flask import Flask
#Applications imports
from .api.routes import api
from .api.urls import *
from .flask_config import app_config

def create_app(conf_name):
    '''
    Init function, create current app and all routes 
    '''
    
    app = Flask(__name__)
    app.config.from_object(app_config[conf_name])
    app_config[conf_name].init_app(app)

    app.register_blueprint(api)
    
    return app
