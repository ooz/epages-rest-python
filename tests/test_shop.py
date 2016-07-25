# -*- coding: utf-8 -*-

import unittest
import os

from context import epages

class TestShop(unittest.TestCase):

    client = None

    @classmethod
    def setUpClass(cls):
        host = os.environ['EPAGES_HOST']
        shop = os.environ['EPAGES_SHOP']
        token = os.environ['EPAGES_TOKEN']
        TestShop.client = epages.HTTPClient(host, shop, token)

    def setUp(self):
        pass

    def test_shop(self):
        shop_service = epages.ShopService(TestShop.client)

        shop = shop_service.get_shop()
        currencies = shop_service.get_currencies()
        locales = shop_service.get_locales()

        self.assertTrue(unicode(shop).startswith(u"Shop("), u"Shops should be created.")
        self.assertEqual(unicode(currencies), u"Currencies(GBP, [u'EUR', u'GBP', u'DKK', u'NOK', u'RUB', u'SEK'])")
        self.assertEqual(unicode(locales), u"Locales(en_GB, [u'de_DE', u'en_GB', u'en_US', u'en_AU', u'en_CA', u'en_NZ', u'en_IE', u'ru_RU', u'it_IT', u'nl_NL', u'fi_FI', u'pt_PT', u'fr_FR', u'sv_SE', u'es_ES', u'ca_ES'])")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
