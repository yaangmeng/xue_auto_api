#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: test_user.py
# 创建时间: 2021/8/8 13:11

from common.send_request import SendRequest


def test_login():
    res = SendRequest().send_request("test_case/登录.json")
    print(res.http_request)
    print(res.http_response)

