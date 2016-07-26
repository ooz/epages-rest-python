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

    _URI_SEP = u"/"

    def __init__(self, api_url, token=u""):
        """Initializer.
        Args:
            api_url: The epages API URL containing the shops domain and shop
                     name. Usually looks like this:
                     https://your.domain.com/rs/shops/yourShopName
            token:   The OAUTH2 security token. Default: empty unicode.
                     If empty: don't perform authorization.
        """
        super(HTTPClient, self).__init__()

        self.api_url = api_url
        self.token = token

        # Construct default headers
        self._default_headers = {}
        self._default_headers["Accept"] = u"application/vnd.epages.v1+json"
        self._default_headers["Content-Type"] = u"application/json"
        if self.token != u"":
            self._default_headers["Authorization"] = "Bearer " + self.token

        # Remove trailing / from api_url
        if self.api_url.endswith(HTTPClient._URI_SEP):
            self.api_url = self.api_url[:-1]

    def get(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.get, ressource, headers, params, json)

    def post(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.post, ressource, headers, params, json)

    def put(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.put, ressource, headers, params, json)

    def delete(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.delete, ressource, headers, params, json)

    def patch(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.patch, ressource, headers, params, json)

    def _request(self, method, ressource=u"", headers=None, params=None, json=None):
        """Executes a HTTP request.
        Args:
            ressource (unicode): URI of the ressource.
            headers (dict): Header dictionary or None. Default: None.
            params (dict): Parameters dictionary or None. Default: None.
            json (dict): JSON payload/data dictionary or None. Default: None.
        Return:
            JSON response. If it's a 204 (No Content) response, the HTTP status
            code is returned.
        """
        headers = headers or {}
        params = params or {}
        json = json or {}

        target_headers = self._default_headers.copy()
        target_headers.update(headers)

        target_url = self.api_url + ressource

        response = method(target_url, headers=target_headers, params=params, json=json)

        # Check for 4xx or 5xx HTTP errors
        if str(response.status_code)[0] in ["4", "5"]:
            raise RESTError(response)
        if response.status_code in [204]:
            return response.status_code
        return response.json()
