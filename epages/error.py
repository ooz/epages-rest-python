# coding: utf-8

class RESTError(Exception):
    """docstring for RESTError"""
    def __init__(self, response=None):
        super(RESTError, self).__init__()
        self.json = None
        self.text = None
        if response is not None:
            try:
                self.json = response.json()
            except:
                self.text = response.text

    def __unicode__(self):
        if self.json is not None:
            return u"RESTError(%s)" % unicode(self.json)
        else:
            return u"RESTError(\n%s\n)" % unicode(self.text)
