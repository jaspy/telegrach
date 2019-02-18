from flask import jsonify, request
import json
from app.models import PostsTest

def get_data_from_json():
    '''
    Transform JSON to dict

    Args:
        None
    Returns:
        Dict with key-value of JSON fields
        if passed not valid JSON:
            None
    '''
    try: 
        data = json.loads(request.get_data())
        return data
    except json.decoder.JSONDecodeError:
        return None

def get_object_by_slug(slug):
    '''
    Get post from database by passing slug
    
    Args:
        slug (str): Value of field 'slug'

    Returns:
        post with current slug

        if passed not existing slug:
            None
    '''
    try:
        obj = PostsTest.objects(slug__exact=slug)[0]
        return obj
    except IndexError:
        return None 
   