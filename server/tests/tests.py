import unittest
from app import create_app
from app.models import PostsTest
from flask import current_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        # with switch_db(PostsTest, 'test_db') as PostsTest:
        #     pass
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        PostsTest.drop_collection()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_api_some_behavior(self):
        pass