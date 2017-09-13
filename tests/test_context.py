# -*- coding: utf-8 -*-

from tests.context import given_any_epages_shop, EPAGES_API_URL, EPAGES_TOKEN

def test_if_any_shop_is_present():
    given_any_epages_shop()

    # then
    assert EPAGES_API_URL != '', 'EPAGES_API_URL was expected to be set!'
    assert EPAGES_TOKEN != '', 'EPAGES_TOKEN was expected to be set!'
