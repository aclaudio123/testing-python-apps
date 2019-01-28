# Unit test for the blog.py

from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    # test3 -
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)

        # test the number of posts (posts length)
        # self.assert.Equal(len([]), len(b.post))
        # self.assert.Equal(0, len(b.post))
        self.assertListEqual([], b.posts)

    # test4: string representation of 0 post by object
    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'John Smith')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by John Smith (0 posts)')

    # test5: string representation of multiple posts
    def test_repr_multiple(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['post1']
        b2 = Blog('My Day', 'John Smith')
        b2.posts = ['post1', 'post2', 'post3']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual('My Day by John Smith (3 posts)', b2.__repr__())











