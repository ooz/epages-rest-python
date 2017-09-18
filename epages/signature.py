# -*- coding: utf-8 -*-

import hmac
import hashlib
import base64

def calculate_signature(code, access_token_url, client_secret):
    message = '%s:%s' % (code, access_token_url)
    digest = hmac.new(client_secret, msg=message, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode()

def verify_signature(code, access_token_url, client_secret, signature):
    return signature == calculate_signature(code, access_token_url, client_secret)

