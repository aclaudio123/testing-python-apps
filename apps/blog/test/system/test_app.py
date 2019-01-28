# System test for the application
# System test is for testing the entire system, everything the user interacts with

from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

# Mocking and patching
# a way to capture functions that display output to console
# in order to assert what's being printed is correct
from post import Post


class AppTest(TestCase):

    def setUp(self):
        blog = Blog('My Blog', 'John Smith')  # creating a blog object
        app.blogs = {'My Blog': blog}

        # test the selections
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_ask_create_blog.assert_called()

    # assert prompt message in input() is being printed
    def test_menu_prints_prompt(self):
        # capture the function we interested in mocking
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)  # assert mock called with expected output

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('My Blog by John Smith (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = {'My Blog', 'John Smith'}
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs['My Blog'])

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='My Blog'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['My Blog'])

    def test_print_posts(self):
        app.blogs['My Blog'].create_post('Test Post', 'Test Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['My Blog'])

            mocked_print_post.assert_called_with(app.blogs['My Blog'].posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
--- Post title ---

Post content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('My Blog', 'Test Title', 'Test Content')
            app.ask_create_post()

            self.assertEqual(app.blogs['My Blog'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['My Blog'].posts[0].content, 'Test Content')

