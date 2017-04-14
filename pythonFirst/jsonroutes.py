#!/bin/env python
#-*- encoding=utf8 -*-

import logic.groupJsonHandler
import logic.groupElementJsonHandler
import logic.contentJsonHandler

HANDLER_MAP = {
    #'sendcode': logic.api.userhandler.SendCode,
    # "ReqkeyWordList":logic.keywordListJsonHandler.KeywordListJsonHandler,
    # 'ReqEditkeyWord':logic.editkeyWordJsonHandler.EditkeyWordJsonHandler,
    # 'ReqSearchkeyWord':logic.searchkeyWordJsonHandler.SearchkeyWordJsonHandler,
    # 'ReqCheckList':logic.checkListJsonHandler.CheckListJsonHandler,
    # 'ReqAccessList':logic.accessListJsonHandler.AccessListJsonHandler,
    # 'ReqLogin':logic.loginJsonHandler.LoginJsonHandler,
    'ReqGroupList':logic.groupJsonHandler.GroupJsonHandler,
    'ReqGroupElementList':logic.groupElementJsonHandler.GroupElementJsonHandler,
    'ReqContent':logic.contentJsonHandler.ContentJsonHandler,
}