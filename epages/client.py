# coding: utf-8
'''
Author: Oliver Zscheyge
Description:
    Provides the REST client to connect to the ePages REST API.
'''

import requests

from epages.error import RESTError

class HTTPClient(object):
    """Client to connect to the ePages REST API.
    """

    _HTTP = u"http://"
    _HTTPS = u"https://"
    _URI_SEP = u"/"

    def __init__(self, host, shop, token=u"", ssl=True):
        """Initializer.
        Args:
            host:  The host URL, e.g. www.example.com as unicode.
            shop:  The ePages shop name as unicode.
            token: The OAUTH2 security token. Default: empty unicode.
                   If empty: don't perform authorization.
            ssl:   Flag whether to use SSL encryption. Default: True.
        """
        super(HTTPClient, self).__init__()
        self._host = host
        self._shop = shop
        self._token = token
        self._default_headers = {}
        self._default_headers["Accept"] = u"application/vnd.epages.v1+json"
        self._default_headers["Content-Type"] = u"application/json"

        # Remove protocol from host
        if self._host.startswith(HTTPClient._HTTP):
            self._host = self._host.replace(HTTPClient._HTTP, u"")
        elif self._host.startswith(HTTPClient._HTTPS):
            self._host = self._host.replace(HTTPClient._HTTPS, u"")

        # Remove trailing / from host
        if self._host.endswith(HTTPClient._URI_SEP):
            self._host = self._host[:-1]

        self._protocol = HTTPClient._HTTP
        if ssl:
            self._protocol = HTTPClient._HTTPS


    def get(self, ressource=u"", headers=None, params=None):
        return self._request(requests.get, ressource, headers, params)

    def post(self, ressource=u"", headers=None, params=None):
        return self._request(requests.post, ressource, headers, params)

    def put(self, ressource=u"", headers=None, params=None):
        return self._request(requests.put, ressource, headers, params)

    def delete(self, ressource=u"", headers=None, params=None):
        return self._request(requests.delete, ressource, headers, params)

    def patch(self, ressource=u"", headers=None, params=None):
        return self._request(requests.patch, ressource, headers, params)

    def _request(self, method, ressource=u"", headers=None, params=None):
        """Executes a HTTP request.
        Args:
            ressource (unicode): URI of the ressource.
            headers (dict): Header dictionary or None. Default: None.
            params (dict): Parameters dictionary or None. Default: None.
        Return:
            JSON response.
        """
        headers = headers or {}
        params = params or {}

        target_headers = self._default_headers.copy()
        target_headers.update(headers)
        if self._protocol == HTTPClient._HTTPS:
            target_headers["Authorization"] = "Bearer " + self._token
        target_url = self._protocol + self._host + u"/rs/shops/" + self._shop + ressource

        response = method(target_url, headers=target_headers, params=params)

        # Check for 4xx or 5xx HTTP errors
        if str(response.status_code)[0] in ["4", "5"]:
            raise RESTError(response.json())
        return response.json()


if __name__ == '__main__':
    print u"Testing " + __file__
