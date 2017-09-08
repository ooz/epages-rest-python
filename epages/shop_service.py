# coding: utf-8
'''
Author: Oliver Zscheyge
Description:
    Provides access to all the shop related calls provided by the epages REST API.
'''

from epages.shop import Shop, Currencies, Locales
from epages.error import RESTError

class ShopService(object):
    """A call to a method of this class results in one epages API call.
    """

    def __init__(self, client):
        """Initializer.
        Args:
            client (HTTPClient): The HTTPClient to make the HTTP calls with.
        """
        super(ShopService, self).__init__()
        self.client = client

    def get_shop(self, locale=u""):
        """Gets the Shop object.
        Args:
            locale (unicode): Optional locale of the Shop object. If set,
                              attributes like the slogan are localized.
        Return:
            Shop: Shop object or None if there was an error.
        """
        params = {}
        if locale != u"":
            params = {
                u"locale": locale
            }

        try:
            json_shop = self.client.get(params=params)
            return Shop(json_shop.get(u"name", u""),
                        json_shop.get(u"slogan", u""),
                        json_shop.get(u"logoUrl", u""),
                        json_shop.get(u"sfUrl", u""),
                        json_shop.get(u"mboUrl", u""))
        except RESTError as error:
            print(unicode(error))
            return None

    def get_currencies(self):
        """Gets the Currencies object associated with the shop.
        Return:
            Currencies: Currencies object listing the default currency and all
                        available currencies of the shop.
                        None if there was an error.
        """
        try:
            json_currencies = self.client.get(u"/currencies")
            return Currencies(json_currencies[u"default"],
                              json_currencies[u"items"])
        except RESTError as error:
            print(unicode(error))
            return None

    def get_locales(self):
        """Gets the Locales object of the shop.
        Return:
            Locales: Locales object providing the default locale and all locales
                     available in the shop.
                     None if there was an error.
        """
        try:
            json_locales = self.client.get(u"/locales")
            return Locales(json_locales[u"default"],
                           json_locales[u"items"])
        except RESTError as error:
            print(unicode(error))
            return None
