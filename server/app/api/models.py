from mongoengine import *
from time import time
from pytils.translit import slugify

def create_slug(title):
    return slugify(f'{title}-{int(time())}')


class PostsTest(Document):
    """
    There will be docstring for it class soon
    """    
    username = StringField(max_length=50, required=True)
    title = StringField(max_length=150, required=True)
    body = StringField(max_length=800)
    slug = StringField(max_length=200)
    hash_ = StringField(max_length=200)

    def as_dict(self):
        return {
            "slug": self.slug,
            "username": self.username,
            "title": self.title,
            "body": self.body,
            "hash": self.hash_,
        }
