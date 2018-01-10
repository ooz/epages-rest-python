# -*- coding: utf-8 -*-
'''
description: Tests signature calculation and verification
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''
from tests.context import epages

CODE = 'rp6YlWEcSxS81OTmdksLOaqv7TRbpzSV'
ACCESS_TOKEN_URL = 'https://devshop.epages.com/rs/shops/lingering-hill-2037/token'
CLIENT_SECRET = 'pM8vwvhYTNMErQsNSJZ0wr91ucOmL5JI'
SIGNATURE = 'g1L73Mv6GnUE8vfWHmxKQmG9KuLiwwI9LMR50w+SXTo='


def test_calculate_signature():
    assert epages.calculate_signature(
        CODE, ACCESS_TOKEN_URL, CLIENT_SECRET) == SIGNATURE.encode('utf-8')


def test_verify_signature():
    assert epages.verify_signature(
        CODE, ACCESS_TOKEN_URL, CLIENT_SECRET, SIGNATURE)
