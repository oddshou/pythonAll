#!/usr/bin/python
#-*- coding: UTF-8 -*-
from model.baseDid import BaseDid
from dao.contentDao import ContentDao
from bs4 import Comment


class Content(BaseDid):
    """
    主要任务，处理分页内容，
    """
    def __init__(self, id, url):
        BaseDid.__init__(self,url)
        self.id = id
    # def get_pages_content(self):
    #     super(Pages, self).pass_to_bsobj()
    #     soup = self.rootSoup
    #     return soup

    def get_useful_content(self):
        soup = super(Content, self).get_soup_content()
        newlisttag = soup.select(".s_w")
        return newlisttag

    def create_content_dao(self):
        plist = []
        editor = ''
        authos = ''
        title = ''
        #解析内容和编辑信息
        soup = self.get_useful_content()[0]
        for child in soup.find_all('p'):
            #剔除最后一项编辑
            if not child.has_attr('align'):
                plist.append(child.string + "\n")
            #保存编辑信息
            else:
                editor = child.string
        #解析 autho，date
        for heads in soup.select('.s_w_f')[0].strings:
            authos += heads + ' '
        for sss in soup.select('h1')[0]:
            if type(sss)!= Comment:
                title = sss
        contentDao = ContentDao(plist, title, authos, editor, self.id)
        return contentDao.create_dir()


def has_tag_no_class(tag):
    """
    识别包含固定class，但是不包含 style
    :param tag:
    :return:
    """
    return tag.has_attr('class') and not tag.has_attr('style')


def has_tag_no_align(tag):
    """
    识别包含固定class，但是不包含 style
    :param tag:
    :return:
    """
    return tag.has_attr('class') and not tag.has_attr('align')
