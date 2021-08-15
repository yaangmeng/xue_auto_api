#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: base_response.py
# 创建时间: 2021/7/5 9:05

class BaseResponse():

    def __init__(self, response):
        self.response = response

    @property
    def http_response(self):
        status_code = self.response.status_code
        headers = self.response.headers
        text = self.response.text
        from tools.http_tools import dcit_to_kv_header
        from tools.http_tools import format_json
        return f"{status_code}\n{dcit_to_kv_header(headers)}\n\n{format_json(text)}"

    @property
    def http_request(self):
        method = self.response.request.method
        url = self.response.request.url
        headers = self.response.request.headers
        body = self.response.request.body
        from tools.http_tools import dcit_to_kv_header
        from tools.http_tools import format_json
        return f"{method} {url}\n{dcit_to_kv_header(headers)}\n\n{format_json(body)}"
