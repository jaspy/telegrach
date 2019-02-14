from flask import Blueprint, Response, jsonify, request
from app.models import PostsTest
from app.models import create_slug
import json

api = Blueprint('api', __name__) #create Bluprint, they content all routes
                                # what we use in current api 


@api.route("/api/posts", methods=['GET', 'POST'])
def return_posts():
    '''
    returns all posts from database in JSON
    '''
    if request.method == 'POST':
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
    else:
        posts = PostsTest.objects()

        return jsonify([post.as_dict() for post in posts])


@api.route("/api/posts/<slug>", methods=['GET'])
def return_post(slug):
    '''
    returns post whith curent slug in JSON
    '''
    post = PostsTest.objects(slug__exact=slug)

    return jsonify(post[0].as_dict())


@api.route("/api/posts/delete/<int:id>", methods=['POST'])
def delete_post():
    '''
    get id of post for delete, and delete post from database
    '''
    return Response(status=400)