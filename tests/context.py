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

EPAGES_API_URL = ''
EPAGES_TOKEN = ''


def is_epages_base_shop_present():
    return EPAGES_BASE_API_URL != '' and EPAGES_BASE_TOKEN != ''

def is_epages_now_shop_present():
    return EPAGES_NOW_API_URL != '' and EPAGES_NOW_TOKEN != ''

# Initialize convenience globals
if is_epages_base_shop_present():
    EPAGES_API_URL, EPAGES_TOKEN = EPAGES_BASE_API_URL, EPAGES_BASE_TOKEN
if is_epages_now_shop_present():
    EPAGES_API_URL, EPAGES_TOKEN = EPAGES_NOW_API_URL, EPAGES_NOW_TOKEN

def is_any_epages_shop_present():
    return EPAGES_API_URL != '' and EPAGES_TOKEN != ''

@fixture
def given_epages_base_shop():
    assert is_epages_base_shop_present()

@fixture
def given_epages_now_shop():
    assert is_epages_now_shop_present()

@fixture
def given_any_epages_shop():
    assert is_any_epages_shop_present()
