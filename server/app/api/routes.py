from flask import Blueprint, Response, jsonify, request
from app.models import PostsTest
from app.models import create_slug
from .utils import get_data_from_json, get_object_by_slug
import json

api = Blueprint('api', __name__)


def return_posts():
    '''
    GET all posts from database

    Processes GET request, retrieves all objects from 
    the database and returns them in JSON format

    Args:
        None

    Returns:
        JSON response with posts from database    
    '''
    posts = [post.as_dict() for post in PostsTest.objects()]
    
    return jsonify(posts)


def create_post():
    '''
    Create new post in database

    Processes POST request, get JSON with 
    required fields: 'title', 'user', 'body'.
    Combaine JSON to valid data for create
    new post object in database.
    
    Args:
        None
        
    Returns:
        JSON response with created post
        
        if pass non existing key:
            JSON response with {'error': 'Field input Error!'}
        if miss required field:
            JSON response with {'error': 'Field input Error!'}
        if pass more than 3 required field: 
            JSON response with  {'error': 'Expecting 3 fields, passed (number of passed fields)'}
    '''
    data = get_data_from_json() 

    if  data and data.get('title') and data.get('username') and data.get('body'):
 
        title = data.get('title') 
        slug = create_slug(title)

        PostsTest( 
            title=title,
            username=data.get('username'), 
            body=data.get('body'),
            slug=slug,
            hash_=data.get('hash'),
            ).save()    

    else:
        return jsonify({'error': {
            "msg":'Field input error', 
            "code": 400,
            }})
    
    return jsonify(PostsTest.objects(slug__exact=slug)[0].as_dict())


def return_post_by_slug(slug):
    
    '''
    
    GET post by passing slug

    Processes GET request.
    Find object with passed slug.

    Args:
        slug (str): Value of field 'slug'   
     
    Returns:
        JSON response with post who have passed slug

        if passed not existing slug:
            JSON response with: {'error': 'Non existing slug'}
    '''
    post = get_object_by_slug(slug)
    if post:
        return jsonify(post.as_dict())
    else:
        return jsonify({'error': {
            "msg":'Non existing slug', 
            "code": 404,
            }})
        

def delete_post(slug):
    '''
    
    DEIETE post by passing slug

    Processes DELETE request.
    Find object with passed slug and dalete him.

    Args:
        slug (str): Value of field 'slug'   
     
    Returns:
        JSON response with {'massage': 'Successful delete'}

        if passed not existing slug:
            JSON response with: {'error': 'Non existing slug'}
    '''
    post = get_object_by_slug(slug)
    if post:
        post.delete()
        return "Succesfuly deleted", 200
    else:
        return jsonify({'error': {
            "msg":f'Non existing slug {slug}', 
            "code": 404,
            }})
       

def update_post(slug):
    '''
    Update post with passing slug

    Processes POST request, get JSON with 
    required fields: 'title', 'user', 'body'.
    Combaine JSON to valid data for create
    new post object in database.
    
    Args:
        slug (str): Value of field 'slug'
        
    Returns:
        JSON response with created post
        
        if pass non existing key:
            JSON response with: {'error': 'Field input Error!'}
        if miss required field:
            JSON response with: {'error': 'Field input Error!'}
        if pass more than 3 required field: 
            JSON response with: {'error': 'Expecting 3 fields, passed (number of passed fields)'}
        if passed not existing slug:
            JSON response with: {'error': 'Non existing slug'}
    '''
    data = get_data_from_json()
    post = get_object_by_slug(slug)
    
    if not post:
        return jsonify({'error': {
            "msg":'Non existing slug', 
            "code": 404,
            }})

    if all(data.values()): #check entry keys
        post.update(**data)
        post.save()
    else:
        return jsonify({'error': {
            "msg":'Field input error', 
            "code": 400,
            }})

    post = get_object_by_slug(slug)
    
    return jsonify(post.as_dict())
