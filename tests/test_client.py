# -*- coding: utf-8 -*-
'''
description: Tests the ePages RESTClient
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

from tests.context import \
    epages, given_epages_base_shop, EPAGES_BASE_API_URL, EPAGES_BASE_TOKEN, \
    given_epages_byd_shop, \
    EPAGES_BYD_API_URL, EPAGES_BYD_CLIENT_ID, EPAGES_BYD_CLIENT_SECRET


given_epages_base_shop()

API_URL = EPAGES_BASE_API_URL
TOKEN = EPAGES_BASE_TOKEN

client = None


def given_rest_client():
    global client
    client = epages.RESTClient(API_URL, TOKEN)

def test_client_returning_same_for_relative_and_absolute_queries():
    given_rest_client()

    # when
    shop_relative = client.get("/")
    shop_absolute = client.get(API_URL)

    # then
    assert unicode(shop_relative) == unicode(shop_absolute)

def test_detecting_api_url_prefix():
    # given
    api_url = 'https://devshop.epages.com/rs/shops/lingering-hill-2037'
    request_url = 'https://devshop.epages.com/rs/shops/lingering-hill-2037/orders'

    # when
    is_prefix = epages.is_api_url_prefix(request_url, api_url)

    # then
    assert is_prefix

def test_still_detecting_api_url_prefix_despite_epages_now_bug():
    # given
    api_url = 'https://lingering-hill-2037.devshop.epages.com/rs/shops/lingering-hill-2037'
    request_url = 'https://devshop.epages.com/rs/shops/lingering-hill-2037/orders'

    # when
    is_prefix = epages.is_api_url_prefix(request_url, api_url)

    # then
    assert is_prefix

def test_getting_beyond_access_token():
    global client
    given_epages_byd_shop()

    # when
    client = epages.BYDClient(EPAGES_BYD_API_URL,
                              EPAGES_BYD_CLIENT_ID,
                              EPAGES_BYD_CLIENT_SECRET)

    # then
    assert client.beyond, 'Client should be a beyond client!'
    assert client.token != '', 'Beyond client should have a token!'

