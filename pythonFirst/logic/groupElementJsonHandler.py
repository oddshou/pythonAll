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
        groupId = self.request['groupId']
        # for groups in config.GROUP_LIST:
        #     if groups['id'] == self.request['groupId']:
        #          self.response['data'] = dbquery.create_group(
        #              groups['title'], groups['message'], self.request['pageSize'], self.request['pageIndex'])
        if groupId > 0 and groupId <= len(config.GROUP_LIST):
            group = config.GROUP_LIST[groupId - 1]
            self.response['data'] = dbquery.create_group(
                group['title'], group['message'], self.request['pageSize'], self.request['pageIndex'])


