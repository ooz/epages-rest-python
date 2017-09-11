# -*- coding: utf-8 -*-
'''
description: Tests the ePages RESTClient
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

def test_client_returning_same_for_relative_and_absolute_queries():
    given_rest_client()

    shop_relative = client.get("/")
    shop_absolute = client.get(API_URL)

    assert unicode(shop_relative) == unicode(shop_absolute)
