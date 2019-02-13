#  можно убирать

from mongoengine import *
from mongoengine.context_managers import switch_collection
import config

connect(
    db=config.mongodb['db'],
    username=config.mongodb['username'],
    password=config.mongodb['password'],
    host=config.mongodb['host'],
    port=config.mongodb['port'],
)


class Posts(DynamicDocument):
    """
    There will be docstring for it class soon
    """
    title = StringField(max_length=200, required=True)
    body = StringField(max_length=800)


# post1 = Posts(title="title1", body="some text")  # creating new post
# post1.save()  # saving created post to connected database
    
# TODO: to embed mongoengine into Flask
