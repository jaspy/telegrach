from flask import Blueprint, Response, jsonify
from app.models import PostsTest
from app.models import create_slug

api = Blueprint('api', __name__) #create Bluprint, they content all routes
                                # what we use in current api 


@api.route("/api/posts", methods=['GET'])
def return_posts():
    '''
    returns all posts from database in JSON
    '''
    posts = PostsTest.objects()

    return jsonify([post.as_dict() for post in posts])


@api.route("/api/posts/<int:id>", methods=['GET'])
def return_post():
    '''
    return post whith cuurent id  in JSON
    '''
    return Response(status=400)


@api.route("/api/posts/create", methods=['POST'])
def create_post():
    '''
    get data and create new post in database
    '''
    return Response(status=400)


@api.route("/api/posts/delete/<int:id>", methods=['POST'])
def delete_post():
    '''
    get id of post for delete, and delete post from database
    '''
    return Response(status=400)