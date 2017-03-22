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


def print_page_content():
    for i in range(config.PAGE_CONFIG["pages_start"], config.PAGE_CONFIG["pages_end"]):
        print "current page " + str(i)
        page =  Pages(config.ROOT_URLS["root_url"] + config.ROOT_URLS["root_page"] + "page" + str(i) + ".htm")
        # print page.get_soup_content()
        # print page.create_pages_dao()
        #打印titile
        for current_page in page.create_pages_dao():

            print current_page['title']


# demo url    /publish/portal24/tab16992/info848568.htm


def print_content_content():
    content = Content(config.ROOT_URLS["root_url"] + "/publish/portal24/tab16992/info847085.htm")
    content.create_content_dao()

if __name__ == "__main__":
    # print_content_content()
    print_page_content()
