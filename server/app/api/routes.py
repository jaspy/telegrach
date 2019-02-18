from flask import Blueprint, Response, jsonify, request
from app.models import PostsTest
from app.models import create_slug
from .utils import get_data_from_json, get_object_by_slug
import json

api = Blueprint('api', __name__) #create Bluprint, they content all routes
                                # what we use in current api 


def get_posts():
    '''
    GET all posts from database

    Processes GET request, retrieves all objects from 
    the database and returns them in JSON format

    Args:
        None

    Returns:
        JSON response with posts from database    
    '''
    posts = PostsTest.objects()
    return jsonify([post.as_dict() for post in posts])


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

    if  data and data.get('title') and data.get('username') and data.get('body'): #check entry keys
 
        title = data.get('title') 
        slug = create_slug(title)

        PostsTest( 
            title=title,
            username=data.get('username'), 
            body=data.get('body'),
            slug=slug,
            ).save()    

    else:
        return jsonify({'error': 'Field input Error!'})

    if len(data) > 3: #must be equal to 3 because use only 3 required fields
            return jsonify({'error': f'Expecting 3 fields, passed {len(data)}'})
    
    return jsonify(PostsTest.objects(slug__exact=slug)[0].as_dict())#get created post from database


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
        return jsonify({'error': 'Non existing slug'})  

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
        return jsonify({'massage': 'Successful delete'})  
    else:
        return jsonify({'error': 'Non existing slug'})  
       

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
        return jsonify({'error': 'Non existing slug'})

    if data and data.get('title') and data.get('username') and data.get('body'): #check entry keys
        post.update(**data)
        post.save()
    else:
        return jsonify({'error': 'Field input Error!'})

    if len(data) > 3:#must be equal to 3 because use only 3 required fields
        return jsonify({'error': f'Expecting 3 fields, passed {len(data)}'})
    
    return jsonify(post.as_dict())#get uodated post from database
