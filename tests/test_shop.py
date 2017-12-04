# -*- coding: utf-8 -*-
'''
description: Tests the shop resource
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

from tests.context import \
    epages, is_epages_base_shop_present, EPAGES_BASE_API_URL, EPAGES_BASE_TOKEN, \
    is_epages_byd_shop_present, \
    EPAGES_BYD_API_URL, EPAGES_BYD_CLIENT_ID, EPAGES_BYD_CLIENT_SECRET

CLIENT = None

def given_rest_client():
    global CLIENT
    if is_epages_base_shop_present():
        CLIENT = epages.RESTClient(API_URL, TOKEN)

def given_beyond_rest_client():
    global CLIENT
    if is_epages_byd_shop_present():
        CLIENT = epages.BYDClient(EPAGES_BYD_API_URL,
                                  EPAGES_BYD_CLIENT_ID,
                                  EPAGES_BYD_CLIENT_SECRET)

def test_shop():
    if given_rest_client():

        # when
        shop = client.get('/')

        # then
        assert shop['slogan'] != ''
        assert shop['name'] != ''
        assert shop['logoUrl'].startswith('https://')
        assert shop['mboUrl'].startswith('https://')
        assert shop['sfUrl'].startswith('http')
        assert shop['email'] != ''

def test_locales():
    if given_rest_client():

        # when
        locales = client.get('/locales')

        # then
        assert locales['default'] == 'en_GB', \
            'Default devshop should have en_GB as default locale'
        assert 'de_DE' in locales['items'], \
            'Default devshop should support de_DE locale'

def test_currencies():
    if given_rest_client():

        # when
        currencies = client.get('/currencies')

        # then
        assert currencies['default'] == 'GBP', \
            'Default devshop should have GBP as default currency'
        assert 'EUR' in currencies['items'], \
            'Default devshop should support EUR'

def test_beyond_shop():
    if given_beyond_rest_client():

        # when
        shop = client.get('/shop/shop') # This should actually be just '/shop', seems to be a bug in the API

        # then
        assert shop['_id'] != u'', 'Beyond devshop should have an ID!'
        assert shop['name'] != u'', 'Beyond devshop should have a name!'
