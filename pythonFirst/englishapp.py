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
import tornado.ioloop
import tornado.web
import tornado.autoreload


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def add_all_data():
    for i in range(config.PAGE_CONFIG["pages_start"], config.PAGE_CONFIG["pages_end"]):
        print "create page " + str(i)
        page =  Pages(config.ROOT_URLS["root_url"] + config.ROOT_URLS["root_page"] + "page" + str(i) + ".htm", i)
        pages_content_list = page.create_pages_dao()
        print "current page " + str(i) + " end"

        # sort_pages = cnsort(pages)  #不排序直接入库

        # #打印titile
        content_list = create_content_date(pages_content_list)
        dbaction.insert_content(content_list)
        dbaction.insert_all_page(pages_content_list)
        print "insert_page succeed"



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

def create_content_date(page_list_dict):
    content_list = []
    for page_dict in page_list_dict:
        hrefs = ''
        if page_dict['href'].startswith(config.ROOT_URLS["root_url"]) \
            or page_dict['href'].startswith('http') :
            hrefs = page_dict['href']
        else:
            hrefs = config.ROOT_URLS["root_url"] + page_dict['href']
        print "create content page from " + str(page_dict['page']) + " title " + str(page_dict['title'])
        content = Content(page_dict['oid'], hrefs, page_dict['page'])
        content_dict = content.create_content_dao()
        if content_dict:
            content_list.append(content_dict)
    return content_list

def test_content():
    test_url = 'http://bj.xdf.cn/publish/portal24/tab16992/info667384.htm'
    content = Content('112233', test_url, '60')
    # print "create content page from " + str(page_dict['page'])

    content_dic = content.create_content_dao()
    print content_dic
    # dbaction.insert_content(content_dic)


def run(port=config.GLOBAL_SETTINGS['default_port']):
    # pdb.set_trace()
    import routes

    application = tornado.web.Application(routes.URL_PATTERN, **config.TORNADO_SETTINGS)
    application.listen(port, xheaders=True)
    print port
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()

if __name__ == "__main__":
    if config.GLOBAL_SETTINGS['get_data']:
        add_all_data()
    else:
        if len(sys.argv) > 1:
            run(int(sys.argv[1]))
        else:
            run()
