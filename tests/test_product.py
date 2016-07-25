# -*- coding: utf-8 -*-

import unittest
import os

from context import epages

class TestProduct(unittest.TestCase):

    client = None
    product_service = None
    product_id = None

    @classmethod
    def setUpClass(cls):
        host = os.environ['EPAGES_HOST']
        shop = os.environ['EPAGES_SHOP']
        token = os.environ['EPAGES_TOKEN']
        TestProduct.client = epages.HTTPClient(host, shop, token)
        TestProduct.product_service = epages.ProductService(TestProduct.client)

    def setUp(self):
        payload = {
            "productNumber": "1337",
            "name": "epages rest API test product",
            "shortDescription": "Awesome product",
            "description": "This is a brand new product",
            "manufacturer": "Awesome Products Company",
            "price": 13.37,
        }

        params = {
            "locale": "en_GB",
            "currency": "EUR",
        }

        try:
            response = TestProduct.client.post(u"/products", params=params, json=payload)
            TestProduct.product_id = response["productId"]
        except epages.RESTError, error:
            print(unicode(error))

    def test_shop(self):
        pass

    def tearDown(self):
        try:
            if TestProduct.product_id is not None:
                status_code = TestProduct.client.delete(u"/products/" + TestProduct.product_id)
                self.assertEquals(status_code, 204, "DELETE on product should yield 204!")
        except epages.RESTError, error:
            print(unicode(error))

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
