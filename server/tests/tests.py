import unittest
from app import create_app
from app.models import PostsTest, create_slug
from flask import current_app, url_for
from json import loads
from os import environ as cur_env


class ApiTestCase(unittest.TestCase):

    temp_env_vars = {
        'FLASK_CONFIG': 'testing',
        'FLASK_ENV': 'testing',
    }

    def setUp(self):
        self.temp_env_vars['FLASK_CONFIG'], cur_env['FLASK_CONFIG'] = (cur_env['FLASK_CONFIG'], 
                                                                       self.temp_env_vars['FLASK_CONFIG'])

        self.temp_env_vars['FLASK_ENV'], cur_env['FLASK_ENV'] = (cur_env['FLASK_ENV'], 
                                                                 self.temp_env_vars['FLASK_ENV'])

        self.app = create_app('testing')

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        PostsTest.drop_collection()
        self.app_context.pop()

        self.temp_env_vars['FLASK_CONFIG'], cur_env['FLASK_CONFIG'] = (cur_env['FLASK_CONFIG'], 
                                                                       self.temp_env_vars['FLASK_CONFIG'])

        self.temp_env_vars['FLASK_ENV'], cur_env['FLASK_ENV'] = (cur_env['FLASK_ENV'], 
                                                                 self.temp_env_vars['FLASK_ENV'])

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_api_return_posts_view(self):
        """
        Checks the return_posts view returns all posts
        """
        PostsTest(
            title='t1',
            username='@u1', 
            body='b1',
            slug='s1',
            ).save()

        PostsTest(
            title='t2',
            username='@u2', 
            body='b2',
            slug='s2',
            ).save()

        response = self.client.get('api/posts')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            loads(PostsTest.objects().to_json()),
            # [post.as_dict() for post in PostsTest.objects()],
            response.get_json()
        )