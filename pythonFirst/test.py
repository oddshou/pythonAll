#!/usr/bin/python
#-*- coding: UTF-8 -*-

import config
from model.pages import Pages
import utils.hanzisort as hanzi

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def print_title_sort():
    pages = []
    for i in range(config.PAGE_CONFIG["pages_start"], config.PAGE_CONFIG["pages_end"]):
        print "create page " + str(i)
        page =  Pages(config.ROOT_URLS["root_url"] + config.ROOT_URLS["root_page"] + "page" + str(i) + ".htm", i)
        pages.extend(page.create_pages_dao())

    sort_pages = cnsort(pages)
    for page in sort_pages:
        print page['title']


def cnsort(pages):
    """
    对pages的title进行排序
    :param pages:
    :return:
    """
    n = len(pages)
    for i in range(1, n):
        tem_page = pages[i]
        j = i
        while j > 0 and hanzi.comp_char(pages[j - 1]['title'], tem_page['title']):
            pages[j] = pages[j - 1]
            j -= 1
        pages[j] = tem_page
    return pages

# print_title_sort()

import re

compile_str = r'(.*)ll'
match_str = 'hello world, hello oddshou'

pattern = re.compile(compile_str)
match = pattern.match(match_str)
if match:
    print match.group()
    print match.groups()
    print match.pos
    print match.endpos
    print match.lastindex
    print match.lastgroup