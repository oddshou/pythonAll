#!/usr/bin/python
#-*- coding: UTF-8 -*-



# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# print soup.title
# print soup.head
# print soup.a
# print soup.a.string
# print type(soup.a.string)
from collections import Iterable

import config
from model.pages import Pages
from model.content import Content
import utils.hanzisort as hanzi
import allutils.dbaction as dbaction


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def add_all_data():
    pages = []
    for i in range(config.PAGE_CONFIG["pages_start"], config.PAGE_CONFIG["pages_end"]):
        print "current page " + str(i)
        page =  Pages(config.ROOT_URLS["root_url"] + config.ROOT_URLS["root_page"] + "page" + str(i) + ".htm", i)
        pages.extend(page.create_pages_dao())
        print "current page " + str(i) + " end"

    sort_pages = cnsort(pages)
    dbaction.insert_all_page(sort_pages)
    print "insert_all_page succeed"
    # #打印titile
    for current_page in sort_pages:  #完成对title的排序
        print current_page['title']
        add_content_date(current_page)


# demo url    /publish/portal24/tab16992/info848568.htm
def cnsort(pages):
    n = len(pages)
    for i in range(1, n):
        tem_page = pages[i]
        j = i
        while j > 0 and hanzi.comp_char(pages[j - 1]['title'], tem_page['title']):
            pages[j] = pages[j - 1]
            j -= 1
        pages[j] = tem_page
    return pages

def add_content_date(page_dict):
    content = Content(page_dict['oid'], page_dict['href'], page_dict['page'])
    print "create content page from " + str(page_dict['page'])
    content_dic = content.create_content_dao()
    dbaction.insert_content(content_dic)

if __name__ == "__main__":
    # add_content_date()
    add_all_data()
