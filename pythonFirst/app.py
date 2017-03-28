#!/usr/bin/python
#-*- coding: UTF-8 -*-



# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# print soup.title
# print soup.head
# print soup.a
# print soup.a.string
# print type(soup.a.string)


import config
from model.pages import Pages
from model.content import Content
import utils.hanzisort as hanzi


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def print_page_content():
    pages = []
    for i in range(config.PAGE_CONFIG["pages_start"], config.PAGE_CONFIG["pages_end"]):
        print "current page " + str(i)
        page =  Pages(config.ROOT_URLS["root_url"] + config.ROOT_URLS["root_page"] + "page" + str(i) + ".htm")
        pages.extend(page.create_pages_dao())
    #打印titile
    for current_page in cnsort(pages):  #完成对title的排序
        print current_page['title']


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



def print_content_content():
    content = Content(config.ROOT_URLS["root_url"] + "/publish/portal24/tab16992/info847085.htm")
    content.create_content_dao()

if __name__ == "__main__":
    # print_content_content()
    print_page_content()
