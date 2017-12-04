# -*- coding: utf-8 -*-
'''
description: Tests the error handling
author: Oliver Zscheyge <oliverzscheyge@gmail.com>
'''

from tests.context import epages, given_rest_client, given_beyond_rest_client

NOT_FOUND = 404

def test_json_error_for_beyond_shop():
    with given_beyond_rest_client() as client:
        if client is not None:
            try:
                # when
                shop = client.get('/shop/willfail')
            except epages.RESTError, error:
                # then
                assert error.json['status'] == NOT_FOUND

def test_text_error_for_frontend_request():
    with given_beyond_rest_client() as client:
        if client is not None:
            try:
                # when
                shop = client.get('/../failzorproduct/and/category')
            except epages.RESTError, error:
                # then
                assert error.status_code == NOT_FOUND
                assert error.method == 'GET'
                assert error.url.endswith('failzorproduct/and/category')
                assert error.text is not None

