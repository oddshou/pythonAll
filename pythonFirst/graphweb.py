#!/usr/bin/python
#-*- coding: UTF-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getdatafrom(url):
    import urllib2
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    # print  response.read()

    from bs4 import BeautifulSoup
    rootSoup = BeautifulSoup(response.read(), "lxml")
    print rootSoup
    for banner in rootSoup.select(".islider-html"):
        print banner.img.src
     # rootSoup.select(".islider-html")

def getdatafrom(html):
    from bs4 import BeautifulSoup
    rootSoup = BeautifulSoup(open(html))
    print "1获取banner----"
    for banner in rootSoup.select(".islider-html"):
        print banner.find_all('img')[0]['src']
    print "2获取详情----"
    print rootSoup.select('.g-name span')[0].contents[1]
    print "3获取价格----"
    print rootSoup.select('#g-base .g-group-price span')
    print "3.1 团购价格----"
    print rootSoup.select('#g-base .g-group-price')[0].contents[2]
    print "3.2 市场价----"
    print rootSoup.select('#g-base .g-market-price')[0].contents[0].contents[4]
    print "4 商品详情----"
    print rootSoup.select('.goods-details-desc-content')[0].contents[0]
    print "5背景图片----"
    for bag in rootSoup.select('.goods-details .gd-item .gd-img'):
        print bag['data-url']
    print "6购买颜色，尺寸----"
    for color_size in rootSoup.select('.sku-spec-value-list'):
        for color in color_size.contents:
            print color.string
        print "-------------------"
    print "7购买小图----"
    print rootSoup.select('.sku-selector-head')[0].img['src']

if __name__ == "__main__":
    getdatafrom("HTMLs/pinduoduo.html")