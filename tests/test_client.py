# -*- coding: utf-8 -*-

import unittest
import os

from context import epages

class TestClient(unittest.TestCase):

    client = None

    @classmethod
    def setUpClass(cls):
        api_url = os.environ['EPAGES_API_URL']
        token = os.environ['EPAGES_TOKEN']
        TestClient.client = epages.HTTPClient(api_url, token)

    def setUp(self):
        pass

    def test_client(self):
        shop_relative = TestClient.client.get("/")
        shop_absolute = TestClient.client.get(os.environ['EPAGES_API_URL'])

        self.assertEqual(unicode(shop_relative), unicode(shop_absolute))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
