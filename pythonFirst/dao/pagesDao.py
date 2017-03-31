#!/usr/bin/python
#-*- coding: UTF-8 -*-


import config

class PagesDao(object):
    def __init__(self, oid, href, date, title, page):
        self.oid = oid
        self.href = href
        self.date = date
        self.title = title
        self.page = page

    def create_dir(self):
        return {"oid": self.oid, "page": self.page, "href": config.ROOT_URLS["root_url"] + self.href, "date": self.date, "title": self.title}


