# -*- coding: utf-8 -*-
'''
description: Tests the ePages RESTClient
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

from tests.context import \
    epages, EPAGES_BASE_API_URL, \
    is_epages_byd_shop_present, \
    given_rest_client, given_beyond_rest_client

def test_client_returning_same_for_relative_and_absolute_queries():
    with given_rest_client() as client:
        if client is not None:
            # when
            shop_relative = client.get("/")
            shop_absolute = client.get(EPAGES_BASE_API_URL)

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
    with given_beyond_rest_client() as client:
        if client is not None:
            assert client.beyond, 'Client should be a beyond client!'
            assert client.token != '', 'Beyond client should have a token!'

