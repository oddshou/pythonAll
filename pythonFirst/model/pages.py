#!/usr/bin/python
#-*- coding: UTF-8 -*-
from model.baseDid import BaseDid


class Pages(BaseDid):
    """
    主要任务，处理分页内容，
    """
    def __init__(self, url):
        BaseDid.__init__(self, url)

    def getPagesContent(self):
        soup = self.rootSoup
        return soup.title