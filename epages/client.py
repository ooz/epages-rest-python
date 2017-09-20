# coding: utf-8
'''
Author: Oliver Zscheyge
Description:
    Provides the REST client to connect to the ePages REST API.
'''

import requests

from epages.error import RESTError

class RESTClient(object):
    '''Client to connect to the ePages REST API.
    '''

    _URI_SEP = u'/'

    def __init__(self, api_url, token=u"", verify=True, \
                 client_id=u'', client_secret=u'', beyond=False):
        '''Initializer.
        Args:
            api_url: The epages API URL containing the shops domain and shop
                     name. Usually looks like this:
                     https://your.domain.com/rs/shops/yourShopName
            token:   The OAUTH2 security token. Default: empty unicode.
                     If empty: don't perform authorization.
            verify:  SSL certificate validation.
            client_id: Client ID of the app. Needed for beyond auth.
            client_secret: Client secret of the app. Needed for beyond auth.
        '''
        super(RESTClient, self).__init__()

        self._default_headers = {}
        self.api_url = api_url
        self.token = token
        self.verify = verify
        self.client_id = client_id
        self.client_secret = client_secret
        self.beyond = beyond
        if self.beyond:
            self.get_token()

        # Construct default headers
        if self.beyond:
            self._default_headers["Accept"] = u"application/hal+json"
        else:
            self._default_headers["Accept"] = u"application/vnd.epages.v1+json"
            self._default_headers["Content-Type"] = u"application/json"
        if self.token != u"":
            self._default_headers["Authorization"] = "Bearer " + self.token

        # Remove trailing / from api_url
        if self.api_url.endswith(RESTClient._URI_SEP):
            self.api_url = self.api_url[:-1]

    def get_token(self):
        '''ePages Now v2 (Beyond backend) only
        '''
        assert self.beyond and self.client_id != u'' and self.client_secret != u''
        params = {
            'grant_type': 'client_credentials'
        }
        token_response = self.post('/oauth/token',
                                   params=params,
                                   auth=(self.client_id, self.client_secret))
        self.token = token_response.get('access_token', '')
        return self.token

    def get(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.get, ressource, headers, params, json)

    def post(self, ressource=u"", headers=None, params=None, json=None, auth=None):
        return self._request(requests.post, ressource, headers, params, json, auth)

    def put(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.put, ressource, headers, params, json)

    def delete(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.delete, ressource, headers, params, json)

    def patch(self, ressource=u"", headers=None, params=None, json=None):
        return self._request(requests.patch, ressource, headers, params, json)

    def _request(self, method, ressource=u"", headers=None, params=None, json=None, auth=None):
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
        if is_api_url_prefix(ressource, self.api_url):
            target_url = ressource

        response = method(target_url, headers=target_headers, params=params,
                          json=json, verify=self.verify, auth=auth)

        # Check for 4xx or 5xx HTTP errors
        if str(response.status_code)[0] in ["4", "5"]:
            raise RESTError(response)
        if response.status_code in [204]:
            return response.status_code
        return response.json()

class BYDClient(RESTClient):
    '''Convenience for beyond shop clients
    '''
    def __init__(self, api_url, client_id, client_secret):
        super(BYDClient, self).__init__(api_url, \
                                        client_id=client_id, \
                                        client_secret=client_secret, \
                                        beyond=True)


def is_api_url_prefix(request_url, api_url):
    return request_url.startswith(api_url) \
            or _is_epages_now_prefix(request_url, api_url)

def _is_epages_now_prefix(request_url, api_url):
    '''Workaround for a bug in ePages Now
    '''
    import re
    api_url_without_protocol_and_shop_slug = re.sub(r'.*?\.', '', api_url, count=1)
    request_url_without_protocol = re.sub(r'.*://', '', request_url, count=1)
    return request_url_without_protocol.startswith(api_url_without_protocol_and_shop_slug)

