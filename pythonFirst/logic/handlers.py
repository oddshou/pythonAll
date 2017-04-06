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
        if 'exc_info' in kwargs:
            if len(kwargs['exc_info']) >= 3:
                import traceback
                self.write('HTTPError %s' % status_code, traceback.extract_tb(kwargs["exc_info"][2]))
            else:
                self.write('HTTPError %s' % status_code, kwargs['exc_info'])
        # if status_code == 404:
        #     self._dynamic_value['error_code'] = 404
        #     self.generate("error.html")
        # elif status_code >= 500:
        #     self._dynamic_value['error_code'] = 500
        #     self.generate("error.html")