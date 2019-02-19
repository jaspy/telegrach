import unittest
from app import create_app
from app.models import PostsTest, create_slug
from flask import current_app, url_for
from json import loads
import os
from app.flask_config import DevelopmentConfig, TestingConfig


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        PostsTest.drop_collection()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_api_return_posts(self):
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
            # loads(PostsTest.objects().to_json()),
            [post.as_dict() for post in PostsTest.objects()],
            response.get_json()
        )

    def test_api_return_posts_view_empty_db(self):
        """
        If no posts in database return_posts view must return response
        with empty list received by get_json method
        """

        response = self.client.get('api/posts')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [],
            response.get_json()
        )

    def test_api_return_post_by_slug(self):
        """
        return_post_by_slug must return post with specified slug
        """

        slug = 's1'

        post = PostsTest(
            title='t1',
            username='@u1', 
            body='b1',
            slug=slug,
            )
        post.save()

        response = self.client.get(f'api/posts/{slug}')

        self.assertEqual(
            post.as_dict(),
            response.get_json()
        )

    def test_api_return_post_by_slug(self):
        """
        return_post_by_slug must return post with specified slug
        """
        
        slug = 'bad slug'
        response = self.client.get(f'api/posts/{slug}')

        self.assertEqual(
            "Invalid slug",
            response.get_data(as_text=True)
        )
