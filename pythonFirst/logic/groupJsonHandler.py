#!/bin/env python
# -*- encoding=utf8 -*-



import tornado.gen
from logic.jsonhandler import APIBase
# import allutils.dbquery as dbquery
import config

class GroupJsonHandler(APIBase):

    @tornado.gen.coroutine
    def deal(self):


        self.response['rescode'] = 0
        self.response['resmsg'] = '获取成功'
        group_list = []
        for i in range(len(config.GROUP_LIST)):
            new_group = {}
            new_group['id'] = i + 1 #添加id
            for k, v in config.GROUP_LIST[i].items():
                #剔除message
                if not k == 'message':
                    new_group[k] = v
            group_list.append(new_group)
        self.response['data'] = group_list


