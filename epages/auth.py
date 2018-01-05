# -*- coding: utf-8 -*-

import hmac
import hashlib
import base64

from requests import post


def calculate_signature(code, access_token_url, client_secret):
    message = b'%s:%s' % (code, access_token_url)
    digest = hmac.new(client_secret,
                      msg=message,
                      digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest)


def verify_signature(code, access_token_url, client_secret, signature):
    '''Handy
    '''
    return signature == calculate_signature(
        code,
        access_token_url,
        client_secret
    )


def verify_args(client_secret, args):
    '''Handier
    '''
    code = args.get('code', '')
    access_token_url = args.get('access_token_url', '')
    signature = args.get('signature', '')
    return verify_signature(code, access_token_url, client_secret, signature)


def get_access_token(client_id, client_secret, args, verify=True):
    '''Handiest
    All-inclusive solution to all problems™
    '''
    access_token = None
    if verify_args(client_secret, args):
        code = args.get('code', '')
        access_token_url = args.get('access_token_url', '')
        payload = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        try:
            access_token = post(access_token_url, data=payload,
                                verify=verify).json().get('access_token', None)
        except:
            pass

    api_url = args.get('api_url', None)
    return_url = args.get('return_url', None)
    return access_token, api_url, return_url
