# coding: utf-8
'''
Author: Oliver Zscheyge
Description:
    Shop and related classes.
'''

class Shop(object):
    """Class representing an epages shop.
    """

    def __init__(self, name=u"", slogan=u"", logo_url=u"", sf_url=u"", mbo_url=u""):
        """Initializer.
        Args:
            name (unicode): The shop name.
            slogan (unicode): The shop's slogan.
            logo_url (unicode): URL of the shop's logo.
            sf_url (unicode): URL of the shop's storefront.
            mbo_url (unicode): URL of the shop's merchant backoffice.
        """
        super(Shop, self).__init__()
        self.name = name
        self.slogan = slogan
        self.logo_url = logo_url
        self.sf_url = sf_url
        self.mbo_url = mbo_url

    def __unicode__(self):
        return u"Shop(%s, %s, %s, %s, %s)" % (self.name, self.slogan, self.logo_url, self.sf_url, self.mbo_url)

class Currencies(object):
    """Available currencies in an epages shop.
    """

    def __init__(self, default=u"", items=None):
        """Initializer.
        Args:
            default (unicode): The default currency of the shop.
            items (:obj:`list` of :obj:`unicode`): All currencies supported by the shop.
        """
        super(Currencies, self).__init__()
        self.default = default
        self.items = items
        if items is None:
            self.items = []

    def __unicode__(self):
        return u"Currencies(%s, %s)" % (self.default, self.items)

class Locales(object):
    """All locales supported by an epages shop.
    """

    def __init__(self, default=u"", items=None):
        """Initializer.
        Args:
            default (unicode): The default locale of the shop.
            items (:obj:`list` of :obj:`unicode`): All locales supported by the shop.
        """
        super(Locales, self).__init__()
        self.default = default
        self.items = items
        if items is None:
            self.items = []

    def __unicode__(self):
        return u"Locales(%s, %s)" % (self.default, self.items)
