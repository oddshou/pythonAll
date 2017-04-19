#!/bin/env python
# -*- encoding=utf8 -*-

import os

import tornado.web
import tornado.template


class BaseHandler(tornado.web.RequestHandler):
    """
    Tornado请求 Handler 基类，实现了普通HTTP ERROR的异常处理、模板生成功能；
    """
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            super(BaseHandler, self).write_error(status_code, **kwargs)
        # if status_code == 404:
        #     self._dynamic_value['error_code'] = 404
        #     self.generate("error.html")
        # elif status_code >= 500:
        #     self._dynamic_value['error_code'] = 500
        #     self.generate("error.html")
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'content-type, x-requested-with')
        self.set_header('Content-type', 'application/json')