#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask, request, redirect
from requests import post

from epages import get_access_token


app = Flask(__name__)

CLIENT_ID = sys.argv[1]
CLIENT_SECRET = sys.argv[2]


@app.route("/")
def root():
    return "<h1>ePages PythonDemo App</h1>"

@app.route("/callback")
def callback():
    args = request.args
    access_token, api_url, return_url = get_access_token(CLIENT_ID,
                                                         CLIENT_SECRET,
                                                         args)

    if access_token and api_url and return_url:
        print("access_token: %s" % access_token)
        print("api_url: %s" % api_url)
        print("return_url: %s" % return_url)
        return build_redirect(return_url)

    return u'You do not belong here! Ksssh ksssh!', 403

def build_redirect(return_url):
    # Use this for automatic redirect:
    #return redirect(return_url, code=302) # Found
    # Use this for manual return:
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>PythonDemo Callback</title>
</head>
<body>
<h1>Callback</h1>
<p>Thanks for installing PythonDemo App! Hit the "return" link below to return to your MBO/Commerce Cockpit</p>
<a href="%s">return</a>
</body>
</html>
""" % (return_url)


if __name__ == "__main__":
    context = ('cacert.pem', 'privkey.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=False)
