# Unit test for the post.py
# Unit test is test of features that don't depend on anything else
# use to catch any mistakes that can happen after

from unittest import TestCase
from post import Post


class PostTest(TestCase):

    # test 1: test post object creation
    def test_create_post(self):
        # create post object
        p = Post('Test', 'Test Content')

        # use TestCase API to test object
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    # test 2: test sending post as json (dictionary equivalence)
    def test_post_json(self):
        p = Post('Test', 'Test Content')

        # expected json values
        expected = {'title': 'Test', 'content': 'Test Content'}

        # test the key-value pairs
        self.assertDictEqual(expected, p.json())


