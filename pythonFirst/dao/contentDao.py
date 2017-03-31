#!/usr/bin/python
#-*- coding: UTF-8 -*-



class ContentDao(object):
    def __init__(self, plist, title, autho, editor, id, page):
        self.plist = plist
        self.title = title
        self.autho = autho
        self.editor = editor
        self.id = id
        self.page = page

    def create_dir(self):
        return {"plist": self.plist, "autho": self.autho, "title": self.title, "editor": self.editor, "oid": self.id, "page": self.page}


