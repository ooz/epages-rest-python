# -*- coding: utf-8 -*-
'''
description: Tests the shop resource
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

from tests.context import given_rest_client, given_beyond_rest_client

def test_shop():
    with given_rest_client() as client:
        if client is not None:
            # when
            shop = client.get('/')

            # then
            assert shop['name'] != ''
            assert shop['mboUrl'].startswith('https://')
            assert shop['sfUrl'].startswith('http')
            assert shop['email'] != ''

def test_locales():
    with given_rest_client() as client:
        if client is not None:
            # when
            locales = client.get('/locales')

            # then
            assert locales['default'] == 'en_GB', \
                'Default devshop should have en_GB as default locale'
            assert 'en_GB' in locales['items'], \
                'Default devshop should support en_GB locale'

def test_currencies():
    with given_rest_client() as client:
        if client is not None:
            # when
            currencies = client.get('/currencies')

            # then
            assert currencies['default'] == 'EUR', \
                'Default devshop should have EUR as default currency'
            assert 'EUR' in currencies['items'], \
                'Default devshop should support EUR'

def test_beyond_shop():
    with given_beyond_rest_client() as client:
        if client is not None:
            # when
            shop = client.get('/shop')

            # then
            assert shop['_id'] != u'', 'Beyond devshop should have an ID!'
            assert shop['name'] != u'', 'Beyond devshop should have a name!'
