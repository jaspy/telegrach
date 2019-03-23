from flask import Flask
from .flask_config import app_config
import os
# Blueprints
from .api.urls import api
from .static.urls import static

def create_app(conf_name):
    app = Flask(__name__)
    app.config.from_object(app_config[conf_name])
    app_config[conf_name].init_app(app)

    app.register_blueprint(api)
    if os.environ.get('FLASK_ENV') == "production":
        app.register_blueprint(static)
    
    return app
