from mongoengine import *
from . import config
from time import time
from .utils import slugify

connect(
    db=config.mongodb['db'],
    username=config.mongodb['username'],
    password=config.mongodb['password'],
    host=config.mongodb['host'],
    port=config.mongodb['port'],
)


def create_slug(title):
    return slugify(f'{title}-{int(time())}')


class PostsTest(DynamicDocument):
    """
    There will be docstring for it class soon
    """    
    username = StringField(max_length=50, required=True)
    title = StringField(max_length=150, required=True)
    body = StringField(max_length=800)
    slug = StringField(max_length=200)

    def as_dict(self):
        return {
            "slug": self.slug,
            "username": self.username,
            "title": self.title,
            "body": self.body,
        }

if __name__ == "__main__":
    post1 = PostsTest(title="test_post", username="@test_user", body="some text", id_ = create_slug(self.title))
    post1.save()
    