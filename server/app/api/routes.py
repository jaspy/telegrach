from flask import Blueprint, Response, jsonify, request
from app.models import PostsTest
from app.models import create_slug
from .utils import get_data_from_json, get_object_by_slug
import json

api = Blueprint('api', __name__) #create Bluprint, they content all routes
                                # what we use in current api 


def return_posts():
    '''
    returns all posts from database in JSON
    '''
    if PostsTest.objects():
        posts = PostsTest.objects()
        return jsonify([post.as_dict() for post in posts])
    else:
        return jsonify({'massage': 'Post list is empty'})


def create_post():
    '''
    creates new post
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
            ).save()    

    else:
        return jsonify({'error': 'Field input Error!'})

    if len(data) > 3:
            return jsonify({'error': f'Expecting 3 fields, passed {len(data)}'})
    
    return jsonify(PostsTest.objects(slug__exact=slug)[0].as_dict())


def return_post_by_slug(slug):
    '''
    returns post whith curent slug in JSON
    '''
    post = get_object_by_slug(slug)
    if post:
        return jsonify(post[0].as_dict())
    else:
        return jsonify({'error': 'Non existing slug'})  

def delete_post(slug):
    '''
    get id of post for delete, and delete post from database
    '''
    post = get_object_by_slug(slug)
    if post:
        post.delete()
        return jsonify({'massage': 'Successful delete'})  
    else:
        return jsonify({'error': 'Non existing slug'})  
       

def update_post(slug):
    '''
    returns post whith curent slug in JSON
    '''
    data = get_data_from_json()
    post = get_object_by_slug(slug)

    if not post:
        return jsonify({'error': 'Non existing slug'})

    if data and data.get('title') and data.get('username') and data.get('body'):  
        post.update(**data)
        post.save()

    if len(data) > 3:
        return jsonify({'error': f'Expecting 3 fields, passed {len(data)}'})
    
    return jsonify(post.as_dict())
