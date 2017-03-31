#!/usr/bin/python
#-*- coding: UTF-8 -*-
from model.baseDid import BaseDid
from dao.pagesDao import PagesDao



class Pages(BaseDid):
    """
    主要任务，处理分页内容，
    """
    def __init__(self, url, page):
        BaseDid.__init__(self, url)
        self.page = page

    # def get_pages_content(self):
    #     super(Pages, self).pass_to_bsobj()
    #     soup = self.rootSoup
    #     return soup

    def get_useful_content(self):
        soup = super(Pages, self).get_soup_content()
        newlisttag = soup.select(".new_list")
        return newlisttag

    def create_pages_dao(self):
        pages = []
        for child in self.get_useful_content()[0].find_all('li'):
            page = PagesDao(child.a["id"], child.a["href"], child.span.string, child.a["title"], self.page)
            # print page.create_dir()
            pages.append(page.create_dir())
        return pages