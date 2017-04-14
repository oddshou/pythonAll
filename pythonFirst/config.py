#!/usr/bin/python
#-*- coding: UTF-8 -*-
TORNADO_SETTINGS = {
    "debug": True,
    "static_path": '/static',
    "gzip": False,
    "xsrf_cookies": False,
    #"cookie_secret":"",
    # "template_path": "templates",
}

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
    "default_port": 8092,
    "db":{
        'name':'englishs',
        'user':'root',
        'psw':'1234',
        'host':'127.0.0.1:55511'
    },
    "redis": {
        'db': 3,
        'host':'127.0.0.1',
        'port':55501
    },

}
GROUP_LIST =[
    {"id": 1, "title": u'短语', "message": u'……短语……'},
    {"id": 2, "title": u'不定式', "message": u'……不定式……'},
    {"id": 3, "title": u'定语', "message": u'……定语……'},
    {"id": 4, "title": u'动词', "message": u'……动词……'},
    {"id": 5, "title": u'介词', "message": u'……介词……'},
    {"id": 6, "title": u'名词', "message": u'……名词……'},
    {"id": 7, "title": u'形容词', "message": u'……副词……'},
    {"id": 8, "title": u'词的搭配', "message": u'……和……搭配……？……和……有关……？……与……有关……？……与……搭配……'},
    {"id": 9, "title": u'双语美文', "message": u'……美文……？……双语：……？……双语美文……'},
    {"id": 10, "title": u'词句研究', "message": u'……浅论……？……浅谈……'},
    {"id": 11, "title": u'新概念第一册', "message": u'……新概念第一册……？……新概念英语第一册……'},
    {"id": 12, "title": u'新概念第二册', "message": u'……新概念第二册……？……新概念英语第二册……'},
    {"id": 13, "title": u'新概念第三册', "message": u'……新概念第三册……？……新概念英语第三册……'},
    {"id": 14, "title": u'新概念第四册', "message": u'……新概念第四册……？……新概念英语第四册……'},
    {"id": 15, "title": u'新概念语法', "message": u'……新概念语法……？……新概念语句……？……新概念语言点……？……新概念重点句子……'},
    {"id": 16, "title": u'新概念阅读', "message": u'……新概念阅读……'},
    {"id": 17, "title": u'新概念知识点', "message": u'……新概念知识点……'},
    {"id": 18, "title": u'总章', "message": u'……'},


]