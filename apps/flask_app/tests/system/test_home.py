# System test: testing an entire system from the user's point of view
# all functions from flask_app we need to test goes here

from tests.system.base_test import BaseTest
from app import app
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, world!'})
