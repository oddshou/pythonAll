#!/bin/env python
#-*- encoding=utf8 -*-


import config
import allutils.db as db

def insert_all_page(dicts_list):
    """
    批量插入页面数据(多条)
    :param dicts:
    :return:
    """
    if len(dicts_list) <= 0:
        return
    cols = ', '.join(dicts_list[0].keys())
    qmarks = ', '.join(['%s'] * len(dicts_list[0]))
    dicts_value_tuple = (tuple(dict_one.values()) for dict_one in dicts_list)
    sql = 'INSERT INTO %s(%s) VALUES (%s)'% ('pages', cols, qmarks)
    with db.MysqlConnection(config.GLOBAL_SETTINGS['db']) as mysql:
        sql_result = mysql.executemany_rowcount(sql, dicts_value_tuple)
        print sql_result
        if sql_result == len(dicts_list):
            mysql.commit()
    return sql_result

def insert_content(dict_list):
    # new_dict = {"1":2, "2":2, "3":3, "4":[1,2,3,4], "5":[8,7,6,5,4,3,2]}
    """
    对数据库插入字典(单条)
    :param dicts:
    :return:
    """
    tuple_dict_list_value = ()
    for dict_content in dict_list:
        values_list = []
        for value in dict_content.values():
            if isinstance(value, list):
                values_list.append(value_to_string(value))
                pass
            else:
                values_list.append(value)
        tuple_dict_list_value += (values_list,)
    # print values_list
    qmarks = ', '.join(['%s'] * len(dict_list[0]))
    cols = ', '.join(dict_list[0].keys())
    sql = 'INSERT INTO %s(%s) VALUES (%s)'% ('content', cols, qmarks)
    with db.MysqlConnection(config.GLOBAL_SETTINGS['db']) as mysql:
        # sql_result = mysql.execute_rowcount(sql, )
        sql_result = mysql.executemany_rowcount(sql, tuple_dict_list_value)
        print sql_result
        if sql_result == len(dict_list):
            mysql.commit()
    return sql_result


def value_to_string(values):
    value_string = ""
    for value in values:
        #以<p>分隔,原文按段落划分
        value_string += str(value) + '<p>'
    return value_string