#!/bin/env python
# -*- encoding=utf8 -*-



import tornado.gen
from logic.jsonhandler import APIBase
import allutils.dbquery as dbquery
import config

class GroupElementJsonHandler(APIBase):

    @tornado.gen.coroutine
    def deal(self):
        self.check_request([('groupId', "groupId"), ('pageSize', 'pageSize'), ('pageIndex', 'pageIndex')])

        self.response['rescode'] = 0
        self.response['resmsg'] = '获取成功'
        for groups in config.GROUP_LIST:
            if groups['id'] == self.request['groupId']:
                 self.response['data'] = dbquery.create_group(
                     groups['title'], groups['message'], self.request['pageSize'], self.request['pageIndex'])


