# -*- coding: utf-8 -*-

import unittest
import os

from context import epages

#class TestProduct(unittest.TestCase):
#
#    client = None
#    product_service = None
#    product_id = None
#
#    @classmethod
#    def setUpClass(cls):
#        api_url = os.environ['EPAGES_API_URL']
#        token = os.environ['EPAGES_TOKEN']
#        TestProduct.client = epages.HTTPClient(api_url, token)
#        TestProduct.product_service = epages.ProductService(TestProduct.client)
#
#    def setUp(self):
#        payload = {
#            "productNumber": "1337",
#            "name": "epages rest API test product",
#            "shortDescription": "Awesome product",
#            "description": "This is a brand new product",
#            "manufacturer": "Awesome Products Company",
#            "price": 13.37,
#        }
#
#        params = {
#            "locale": "en_GB",
#            "currency": "EUR",
#        }
#
#        try:
#            response = TestProduct.client.post(u"/products", params=params, json=payload)
#            TestProduct.product_id = response["productId"]
#        except epages.RESTError, error:
#            print(unicode(error))
#            self.assertTrue(False, "Setting up a product should not fail!")
#
#    def test_product(self):
#        if TestProduct.product_id is not None:
#            try:
#                product = TestProduct.client.get(u"/products/" + TestProduct.product_id)
#                self.assertEquals(product["productNumber"], "1337", "Product number of created product should match for the requested product.")
#            except epages.RESTError, error:
#                print(unicode(error))
#                self.assertTrue(False, "Getting a product should not fail!")
#
#    def tearDown(self):
#        try:
#            if TestProduct.product_id is not None:
#                status_code = TestProduct.client.delete(u"/products/" + TestProduct.product_id)
#                self.assertEquals(status_code, 204, "DELETE on product should yield 204!")
#        except epages.RESTError, error:
#            print(unicode(error))
#            self.assertTrue(False, "Deleting a product should not fail!")
#
#    @classmethod
#    def tearDownClass(cls):
#        pass

if __name__ == '__main__':
    unittest.main()
