#!/usr/bin/python
#-*- coding: UTF-8 -*-




class BaseDid(object):
    """
    基类，实现URL的解析
    """
    def __init__(self, url):
        self.rootUrl = url
        self._rootSoup = ""

    def get_soup_content(self):
        if not self._rootSoup:
            from bs4 import BeautifulSoup
            import urllib2
            request = urllib2.Request(self.rootUrl)
            response = urllib2.urlopen(request)
            # print  response.read()

            self._rootSoup = BeautifulSoup(response.read(), "lxml")
        return self._rootSoup
