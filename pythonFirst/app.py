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


def printContet():
    page =  Pages(config.ROOT_URLS["root"])
    page.getPagesContent()



if __name__ == "__main__":
    printContet()