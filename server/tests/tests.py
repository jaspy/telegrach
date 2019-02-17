import unittest
from app import create_app
from app.models import PostsTest, create_slug
from flask import current_app, url_for


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        PostsTest.drop_collection()
        self.client = self.app.test_client()

    def tearDown(self):
        PostsTest.drop_collection()
        self.app_context.pop()

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

        response = self.client.get(url_for('return_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            PostsTest.objects().to_json(),
            response.get_data(as_text=True)
        )
