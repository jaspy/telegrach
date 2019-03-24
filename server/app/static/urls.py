import json
from flask import Blueprint, Response, jsonify, request, render_template, url_for, send_from_directory
import os

static = Blueprint('static', __name__, static_folder='../../public')

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../public')

@static.route('/')
def app():
    return send_from_directory(static_file_dir, 'index.html')

@static.route('/<query>')
def app_routes(query):
    return send_from_directory(static_file_dir, 'index.html')

@static.route('/<path:path>')
def static_proxy(path):
    """ static folder serve """
    file_name = path.split('/')[-1]
    dir_name = os.path.join(static_file_dir, '/'.join(path.split('/')[:-1]))
    return send_from_directory(dir_name, file_name)
