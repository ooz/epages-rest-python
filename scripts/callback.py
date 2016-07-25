#!/usr/bin/python
# coding: utf-8

from flask import Flask, request, redirect
from requests import post
import sys
app = Flask(__name__)

CLIENT_ID = sys.argv[1]
CLIENT_SECRET = sys.argv[2]

@app.route("/")
def root():
    return "<h1>drakdrak.ddns.net</h1>"

@app.route("/callback")
def callback():
    args = request.args
    code = args.get("code", "")
    access_token_url = args.get("access_token_url", "")
    api_url = args.get("api_url", "")
    return_url = args.get("return_url", "")

    print("code access_token_url api_url return_url:")
    print(code)
    print(access_token_url)
    print(api_url)
    print(return_url)

    if code != "" and access_token_url != "":
        access_token = get_access_token(code, access_token_url)
        print("Access_token:")
        print(access_token)

    #return redirect(return_url, code=302) # Found
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>PythonDemo Callback</title>
</head>
<body>
<h1>Callback</h1>
<p>Thanks for installing PythonDemo App! Hit the "return" link below to return to your Merchant Backoffice</p>
<a href="%s">return</a>
</body>
</html>
""" % (return_url)

def get_access_token(code, access_token_url):
    payload = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    try:
        response = post(access_token_url, data=payload, verify=False)
        response_json = response.json()
        return response_json.get("access_token", None)
    except:
        pass
    return None


if __name__ == "__main__":
    context = ('cacert.pem', 'privkey.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=False)
