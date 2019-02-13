from flask import Flask
#Applications imports
from .api.routes import api

def create_app():
    '''
    Init function, create current app and all routes 
    '''
    
    app = Flask(__name__)

    app.register_blueprint(api)
    
    return app
