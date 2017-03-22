#!/usr/bin/python
#-*- coding: UTF-8 -*-



class ContentDao(object):
    def __init__(self, plist, title, autho, editor):
        self.plist = plist
        self.title = title
        self.autho = autho
        self.editor = editor

    def create_dir(self):
        return {"plist": self.plist, "autho": self.autho, "title": self.title, "editor": self.editor}


