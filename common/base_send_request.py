#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: base_send_request.py
# 创建时间: 2021/8/1 16:56
import requests

from common.base_request import BaseRequest
from common.base_response import BaseResponse
from common.json_data import JsonData


class BaseSendRequest():

    def send_request(self, req: BaseRequest):
        """
        根据BaseRequest对象，使用requests.request方法完成http请求的发送，并返回一个BaseResponse对象
        :param req: BaseRequest对象
        :return: BaseResponse对象
        """
        d = {}
        d["method"] = req.method
        d["url"] = req.url
        d["headers"] = req.headers
        d["data"] = req.data
        d["json"] = req.json
        d["params"] = req.params
        d["files"] = req.files
        # 使用requests.request() 方法发送请求
        res = requests.request(**d)
        # 实例化一个BaseResponse 对象并返回
        return BaseResponse(res)


if __name__ == '__main__':
    jd = JsonData("test_case/登录.json")
    br = BaseRequest(jd)
    bsr = BaseSendRequest()
    res = bsr.send_request(br)
    print(res.http_request)
    print(res.http_response)
