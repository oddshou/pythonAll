#!/usr/bin/python
#-*- coding: UTF-8 -*-


ROOT_URLS = {
    "root_url": "http://bj.xdf.cn",
    "root_page": "/publish/portal24/tab16992/module100405/"
}

PAGE_CONFIG = {
    "pages_start": 1,
    "pages_end": 75  #75
}

GLOBAL_SETTINGS = {
    "get_data": 0,
    "db":{
        'name':'englishs',
        'user':'root',
        'psw':'1234',
        'host':'127.0.0.1:55511'
    },
    "redis": {
        'db': 1,
        'host':'127.0.0.1',
        'port':55501
    },

}