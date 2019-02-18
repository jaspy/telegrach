from flask import Blueprint, Response, jsonify, request
from app.models import PostsTest
from app.models import create_slug
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
    # return jsonify(json.loads( posts.to_json()) )


def create_post():
    '''
    creates new post
    '''
    try: 
        data = json.loads(request.get_data())
    except json.decoder.JSONDecodeError:
        return jsonify({'error':'misss fild error'})

    if data.get('title') and data.get('username') and data.get('body'):
        if len(data) > 3:
            return jsonify({'error': f'Expecting 3 fields, passed {len(data)}'})

        title = data.get('title')
        slug = create_slug(title)        
        PostsTest(
            title=title,
            username=data.get('username'), 
            body=data.get('body'),
            slug=slug,
            ).save()    

        return jsonify(PostsTest.objects(slug__exact=slug)[0].as_dict())

    else:
        return jsonify({'error': 'Empty field'})


def return_post_by_slug(slug):
    '''
    returns post whith curent slug in JSON
    '''
    try:
        post = PostsTest.objects(slug__exact=slug)[0]
    except IndexError:
        return jsonify({'error': 'Non existing slug'})
    
    return jsonify(post[0].as_dict())


def delete_post(slug):
    '''
    get id of post for delete, and delete post from database
    '''
    try:
        post = PostsTest.objects(slug__exact=slug)[0]
    except IndexError:
        return jsonify({'error': 'Non existing slug'})
    
    post.delete()
    return "Succesfuly deleted"


def update_post(slug):
    '''
    returns post whith curent slug in JSON
    '''
    try: 
        data = json.loads(request.get_data())
    except json.decoder.JSONDecodeError:
        return jsonify({'error':'misss fild error'})
    
    try:
        post = PostsTest.objects(slug__exact=slug)[0]
    except IndexError:
        return jsonify({'error': 'Non existing slug'})
    
    if data.get('title') and data.get('username') and data.get('body'):
        if len(data) > 3:
            return jsonify({'error': f'Expecting 3 fields, passed {len(data)}'})
        
        post.update(**data)
        post.save() 
        return jsonify(post.as_dict())
