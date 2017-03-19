#!/usr/bin/python
#-*- coding: UTF-8 -*-


import urllib2

# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print  response.read()

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")
"""
 或者可以用本地html文件创建对象
"""


# print soup.prettify()
# print soup.title
# print soup.head
print soup.a
print soup.a.string
print type(soup.a.string)