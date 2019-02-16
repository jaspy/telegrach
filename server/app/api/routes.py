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
    posts = PostsTest.objects()

    return jsonify([post.as_dict() for post in posts])


def create_post():
    '''
    creates new post
    '''
    data = json.loads(request.get_data())
    title = data.get('title')
    slug = create_slug(title)        

    PostsTest(
        title=title,
        username=data.get('username'), 
        body=data.get('body'),
        slug=slug,
        ).save()    

    return jsonify(PostsTest.objects(slug__exact=slug)[0].as_dict())


def return_post(slug):
    '''
    returns post whith curent slug in JSON
    '''
    post = PostsTest.objects(slug__exact=slug)

    return jsonify(post[0].as_dict())


def delete_post(slug):
    '''
    get id of post for delete, and delete post from database
    '''

    post1 = PostsTest.objects(slug__exact=slug)[0]
    post1.delete()

    return "Succesfuly deleted"


def update_post(slug):
    '''
    returns post whith curent slug in JSON
    '''
    data = json.loads(request.get_data())

    post1 = PostsTest.objects(slug__exact=slug)[0]
    post1.update(**data)
    post1.save() 

    return jsonify(post1.as_dict())
