# -*- coding: utf-8 -*-
'''
description: ePages REST Python test context
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

import os
import sys

from pytest import fixture

sys.path.insert(0, os.path.abspath('..'))
import epages


EPAGES_BASE_API_URL = os.environ.get('EPAGES_BASE_API_URL', '')
EPAGES_BASE_TOKEN = os.environ.get('EPAGES_BASE_TOKEN', '')

EPAGES_NOW_API_URL = os.environ.get('EPAGES_NOW_API_URL', '')
EPAGES_NOW_TOKEN = os.environ.get('EPAGES_NOW_TOKEN', '')

EPAGES_BYD_API_URL = os.environ.get('EPAGES_BYD_API_URL', '')
EPAGES_BYD_CLIENT_ID = os.environ.get('EPAGES_BYD_CLIENT_ID', '')
EPAGES_BYD_CLIENT_SECRET = os.environ.get('EPAGES_BYD_CLIENT_SECRET', '')

EPAGES_API_URL = ''
EPAGES_TOKEN = ''
EPAGES_CLIENT_ID = ''
EPAGES_CLIENT_SECRET = ''

@fixture
def is_epages_base_shop_present():
    return EPAGES_BASE_API_URL != '' and EPAGES_BASE_TOKEN != ''

@fixture
def is_epages_now_shop_present():
    return EPAGES_NOW_API_URL != '' and EPAGES_NOW_TOKEN != ''

# Initialize convenience globals
if is_epages_base_shop_present():
    EPAGES_API_URL, EPAGES_TOKEN = EPAGES_BASE_API_URL, EPAGES_BASE_TOKEN
if is_epages_now_shop_present():
    EPAGES_API_URL, EPAGES_TOKEN = EPAGES_NOW_API_URL, EPAGES_NOW_TOKEN

@fixture
def is_epages_byd_shop_present():
    return EPAGES_BYD_API_URL != '' and \
           EPAGES_BYD_CLIENT_ID != '' and \
           EPAGES_BYD_CLIENT_SECRET != ''

@fixture
def is_any_epages_shop_present():
    return EPAGES_API_URL != '' and EPAGES_TOKEN != '' or \
            is_epages_byd_shop_present()

# "with" interface implementations
class given_rest_client(object):
    def __enter__(self):
        if is_epages_base_shop_present():
            self.client = epages.RESTClient(EPAGES_BASE_API_URL,
                                            EPAGES_BASE_TOKEN)
            return self.client
        return None

    def __exit__(self, type, value, traceback):
        pass

class given_beyond_rest_client(given_rest_client):
    def __enter__(self):
        if is_epages_byd_shop_present():
            self.client = epages.BYDClient(EPAGES_BYD_API_URL,
                                           EPAGES_BYD_CLIENT_ID,
                                           EPAGES_BYD_CLIENT_SECRET)
            return self.client
        return None
