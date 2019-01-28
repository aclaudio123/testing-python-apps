from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True  # tells flask we in testing mode
        self.app = app.test_client()
