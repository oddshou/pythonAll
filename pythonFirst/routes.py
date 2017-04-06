#!/bin/env python
#-*- encoding=utf8 -*-


import logic.jsonhandler

URL_PATTERN = [
    (r'.*/jsonapi', logic.jsonhandler.JSONHandler),
    (r'.*', logic.jsonhandler.JSONHandler)
]
