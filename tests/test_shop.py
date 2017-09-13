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
    client = epages.RESTClient(API_URL, TOKEN)

def test_shop():
    given_rest_client()

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
    given_rest_client()

    # when
    locales = client.get('/locales')

    # then
    assert locales['default'] == 'en_GB', \
        'Default devshop should have en_GB as default locale'
    assert 'de_DE' in locales['items'], \
        'Default devshop should support de_DE locale'

def test_currencies():
    given_rest_client()

    # when
    currencies = client.get('/currencies')

    # then
    assert currencies['default'] == 'GBP', \
        'Default devshop should have GBP as default currency'
    assert 'EUR' in currencies['items'], \
        'Default devshop should support EUR'
