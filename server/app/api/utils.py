from flask import jsonify, request
import json
from app.models import PostsTest

def get_data_from_json():
    try: 
        data = json.loads(request.get_data())
        return data
    except json.decoder.JSONDecodeError:
        return None

def get_object_by_slug(slug):
    try:
        obj = PostsTest.objects(slug__exact=slug)
        return obj
    except IndexError:
        return None 
   