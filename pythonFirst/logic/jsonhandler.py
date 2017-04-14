#!/bin/env python
# -*- encoding=utf8 -*-

from logic.handlers import BaseHandler

import json
from utils.OJson import OJsonEncoder
import tornado.web
import tornado.gen
from  tornado.httpclient import AsyncHTTPClient, HTTPRequest



class BusinessException(Exception):
    def __init__(self, msg, rescode=1):
        self.msg = msg
        self.rescode = rescode

class JSONHandler(BaseHandler):
    """JSON 协议 Handler（入口）
    """
    def get(self):
        self.write('非法请求')
        self.finish()

    def parse_commm_params(self, request_data={}):
        result = {}
        if 'header' in request_data:
            header = request_data['header']
            result = header
            if 'key' not in header.keys() or self.check_key_error(header['key']):
                raise BusinessException('key error')
        else:
            raise BusinessException('key error')
        return result


    def check_key_error(self, key):
        import hashlib
        src = 'oddskey'
        m2 = hashlib.md5()
        m2.update(src)
        return m2.hexdigest() != key    #27a5ddfd5c81a95502fcbaab47379277

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        try:
            post_data = self.request.body
            self.set_header("Access-Control-Allow-Origin", "*")
            if post_data:
                request = json.loads(post_data)

                # 单个API请求
                if request and 'api' in request and 'params' in request:
                    method = request['api']
                    import jsonroutes
                    handler_map = jsonroutes.HANDLER_MAP
                    if method in handler_map:
                        handler = handler_map[method]()
                        handler.request = request['params']
                        handler.method = method
                        handler.tornado_handler = self
                        # handler.logger = self.logger
                        handler.comm_args = self.parse_commm_params(request)

                        yield handler.deal()
                        self.write(json.dumps(handler.response, cls=OJsonEncoder))
                        self.finish()
                    else:
                        raise BusinessException("Api Not Exist!")

                # # 多个API请求
                # elif request and 'apilist' in request:
                #     apilist = request['apilist']
                #     import jsonroutes
                #     reslist_result = dict(rescode=0,resmsg='',reslist=[])
                #     for each_req in apilist:
                #         method = each_req['api']
                #         handler_map = jsonroutes.HANDLER_MAP
                #         try:
                #             if method in handler_map:
                #                 handler = handler_map[method]()
                #                 handler.request = each_req['params']
                #                 handler.method = method
                #                 handler.tornado_handler = self
                #                 handler.logger = self.logger
                #                 handler.comm_args = self.parse_commm_params(request)
                #
                #                 yield handler.deal()
                #                 reslist_result['reslist'].append(handler.response)
                #             else:
                #                 raise BusinessException("Api Not Exist!")
                #
                #         except BusinessException, e:
                #             response = {'rescode': 1, 'resmsg': 'success'}
                #             response['resmsg'] = e.msg
                #             response['rescode'] = e.rescode
                #             reslist_result['reslist'].append(response)
                #
                #     self.write(json.dumps(reslist_result))
                #     self.finish()

                else:
                    self.write('Wrong Request')
                    self.finish()
            else:
                self.write('Wrong Request')
                self.finish()
        except BusinessException, e:
            import traceback
            traceback.print_exc()
            response = {'rescode': 1, 'resmsg': 'success'}
            response['resmsg'] = e.msg
            response['rescode'] = e.rescode
            self.write(json.dumps(response))
            self.finish()
        except Exception, e:
            import traceback
            traceback.print_exc()
            # self.logger.write('post', e)
            response = {'rescode': 1, 'resmsg': 'exception'}
            self.write(json.dumps(response))
            self.finish()


class APIBase(object):
    def __init__(self):
        self.request = {}
        self.method = ''
        self.response = {'rescode': -1, 'resmsg': 'fail'}

    def check_request(self, param_list):
        """检查是否包含必传参数
        """
        for key,name in param_list:
            if key not in self.request:
                raise BusinessException('%s不能为空或注意大小写' % name)

    def deal(self):
        # 未实现
        raise NotImplementedError("")
