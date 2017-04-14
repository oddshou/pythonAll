#!/bin/env python
# -*- encoding=utf8 -*-



import tornado.gen
from logic.jsonhandler import APIBase
import allutils.dbquery as dbquery
import config

class ContentJsonHandler(APIBase):

    @tornado.gen.coroutine
    def deal(self):
        self.check_request([('oid', 'oid')])

        self.response['rescode'] = 0
        self.response['resmsg'] = '获取成功'
        self.response['data'] = dbquery.query_content(self.request['oid'])




