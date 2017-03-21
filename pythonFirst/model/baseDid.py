#!/usr/bin/python
#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

import urllib2


class BaseDid(object):
    """
    基类，实现URL的解析
    """
    def __init__(self, url):
        self.rootUrl = url;

    def pass_to_bsobj(self):
        request = urllib2.Request(self.rootUrl)
        response = urllib2.urlopen(request)
        # print  response.read()

        self.rootSoup = BeautifulSoup(response.read(), "lxml")
