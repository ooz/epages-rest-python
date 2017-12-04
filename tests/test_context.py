# -*- coding: utf-8 -*-

from tests.context import is_any_epages_shop_present, EPAGES_API_URL, EPAGES_TOKEN, \
        is_epages_base_shop_present, is_epages_now_shop_present

def test_if_any_shop_is_present():
    assert is_any_epages_shop_present()

def test_if_api_url_and_token_are_set_for_base_and_now_shops():
    if is_epages_base_shop_present() or is_epages_now_shop_present():
        assert EPAGES_API_URL != '', 'EPAGES_API_URL was expected to be set!'
        assert EPAGES_TOKEN != '', 'EPAGES_TOKEN was expected to be set!'
