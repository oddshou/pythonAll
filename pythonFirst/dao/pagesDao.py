#!/usr/bin/python
#-*- coding: UTF-8 -*-



class PagesDao(object):
    def __init__(self, oid, href, date, title):
        self.oid = oid
        self.href = href
        self.date = date
        self.title = title

    def create_dir(self):
        return {"oid": self.oid, "href": self.href, "date": self.date, "title": self.title}


