# все менять

from flask import jsonify
from .models import PostsTest
from . import app
from .models import create_slug


@app.route('/')
def index():
    # title = "post1"
    # post1 = PostsTest(title=title, username="@test_user", body="some text lorem", slug=create_slug(title))
    # post1.save()
    return '<h1>Hello</h1>'


@app.route('/posts/', methods=['GET'])
def posts():
    posts = PostsTest.objects()
    return jsonify([post.as_dict() for post in posts])