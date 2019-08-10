import urllib
from typing import Dict
from unittest import TestCase
from app import application


class Base(TestCase):
    def setUp(self):
        application.config['RUN_MODE'] = 'test'
        application.config.from_object('app.config.test.Config')

        self.app = application.test_client(self)
        self.app_context = application.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def api_get(self, path: str, query: Dict = None):
        # TODO: query string
        url = f'{path}?{urllib.parse.urlencode(query)}' if query else path
        return self.app.get(url, **{})
