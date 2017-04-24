#!/bin/env python
#-*- encoding=utf8 -*-

import allutils.db as db
import config
import re


def create_pattern(pattern_string):
    """
    # import re
    #
    # compile_str = ur'英语(.*)三'
    # print type(compile_str)
    # match_str = unicode('新概念英语语法讲解三章，第三节-lesson5','utf-8')
    # print type(match_str)
    # pattern = re.compile(compile_str)
    # match = pattern.search(match_str)
    # if match:
    #     print match.group()
    #     print match.groups()
    #     print match.pos
    #     print match.endpos
    #     print match.lastindex
    #     print match.lastgroup

    :param pattern_string:
    :return:
    """
    pattern_list = re.split(ur'？|\?', pattern_string)
    new_pattern_list = []
    for pattern in pattern_list:
        new_pattern_list.append(pattern.replace(u'……', u'(.*)'))
    all_pattern = '|'.join(new_pattern_list)
    # print all_pattern
    return all_pattern

def create_group(group_title, group_pattern, pageSize, pageIndex):
    """
    创建分组
    说明："?"号表示"或者"  "*"表示任意字符
    :param group_title: 分组名
    :param group_pattern: 分组原则
    :return:
    """
    #1.获取title 列表
    #2.对titile 列表使用正则表达式进行匹配
    #3.返回匹配的title
    patterns = create_pattern(group_pattern)
    select_sql = """select * from pages where title regexp %s;"""
    with db.MysqlConnection(config.GLOBAL_SETTINGS['db']) as mysql:
        query_data = mysql.query(select_sql, patterns)
        if len(query_data) > pageSize*pageIndex and len(query_data) > pageSize * (pageIndex + 1):
            return query_data[(pageSize*pageIndex): pageSize*(pageIndex + 1)]
        elif len(query_data) > pageSize*pageIndex and len(query_data) <= pageSize * (pageIndex + 1):
            return query_data[(pageSize*pageIndex):]
        else:
            return {}


# group_pattern = u'……短语……？语法'
# group_title = u'短语'
# create_group(group_title, group_pattern)

def query_content(oid):
    select_sql = """select * from content where oid=%s"""
    with db.MysqlConnection(config.GLOBAL_SETTINGS['db']) as mysql:
        query_data = mysql.query(select_sql, oid)
        if query_data:
            return query_data[0]