# Integration test for the blog.py
# Integration test is testing a feature that depends on another feature
# In this case the blog depends on post

from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    # test1: test creating a post in blog
    def test_create_post_in_blog(self):
        b = Blog('My Day', 'John Smith')
        b.create_post('Post Title', 'Post Content')

        self.assertEqual('Post Title', b.posts[0].title)
        self.assertEqual('Post Content', b.posts[0].content)

    # test2: test json representation of blog with no post
    def test_json_with_no_posts(self):
        b = Blog('My Blog', 'John Smith')

        expected = {'title': 'My Blog',
                    'author': 'John Smith',
                    'posts': []
                    }
        self.assertDictEqual(expected, b.json())

    # test2: test json representation of blog with no post
    def test_json(self):
        b = Blog('My Blog', 'John Smith')
        b.create_post('Post Title', 'Post Content')

        expected = {'title': 'My Blog',
                    'author': 'John Smith',
                    'posts': [{'title': 'Post Title',
                               'content': 'Post Content'}
                              ],
                    }
        self.assertDictEqual(expected, b.json())
