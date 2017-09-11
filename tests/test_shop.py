# -*- coding: utf-8 -*-
'''
description: Tests the shop resource
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

from tests.context import \
    epages, given_epages_base_shop, EPAGES_BASE_API_URL, EPAGES_BASE_TOKEN


given_epages_base_shop()

API_URL = EPAGES_BASE_API_URL
TOKEN = EPAGES_BASE_TOKEN

client = None


def given_rest_client():
    global client
    client = epages.HTTPClient(API_URL, TOKEN)

def test_shop_service():
    given_rest_client()

    shop_service = epages.ShopService(client)
    shop = shop_service.get_shop()
    currencies = shop_service.get_currencies()
    locales = shop_service.get_locales()

    assert unicode(shop).startswith(u"Shop("), u"Shop object should be created."
    assert \
        unicode(currencies) == \
            u"Currencies(GBP, [u'EUR', u'GBP', u'DKK', u'NOK', u'RUB', u'SEK'])"
    assert \
        unicode(locales).startswith(u"Locales(en_GB, [u'de_DE'")
