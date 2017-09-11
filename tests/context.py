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


EPAGES_BASE_API_URL = os.environ['EPAGES_BASE_API_URL']
EPAGES_BASE_TOKEN = os.environ['EPAGES_BASE_TOKEN']

EPAGES_NOW_API_URL = os.environ['EPAGES_NOW_API_URL']
EPAGES_NOW_TOKEN = os.environ['EPAGES_NOW_TOKEN']

@fixture
def given_epages_base_shop():
    assert EPAGES_BASE_API_URL != ""
    assert EPAGES_BASE_TOKEN != ""

@fixture
def given_epages_now_shop():
    assert EPAGES_NOW_API_URL != ""
    assert EPAGES_NOW_TOKEN != ""
