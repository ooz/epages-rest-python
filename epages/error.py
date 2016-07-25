# coding: utf-8

class RESTError(Exception):
    """docstring for RESTError"""
    def __init__(self, json={}):
        super(RESTError, self).__init__()
        self.json = json

    def __unicode__(self):
        return u"RESTError(%s)" % unicode(self.json)
