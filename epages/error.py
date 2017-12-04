# coding: utf-8

class RESTError(Exception):
    """docstring for RESTError"""
    def __init__(self, response=None):
        super(RESTError, self).__init__()
        self.status_code = None
        self.json = None
        self.text = None
        self.method = None
        self.url = None
        if response is not None:
            self.status_code = response.status_code
            try:
                self.json = response.json()
            except:
                self.text = response.text
            request = response.request
            if request is not None:
                self.method = request.method
                self.url = request.url

    def __unicode__(self):
        if self.json is not None:
            return u"RESTError(%s)" % unicode(self.json)
        else:
            return u"""RESTError(
%s - %s %s
%s
)""" % (self.status_code, self.method, self.url, unicode(self.text))
