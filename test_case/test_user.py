#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: test_user.py
# 创建时间: 2021/8/8 13:11
import pytest

from common.send_request import SendRequest

file_list=[
    "test_case/注册.json",
    "test_case/登录.json",
    "test_case/商品搜索.json",
    "test_case/添加购物车.json",
    "test_case/查询购物车列表.json",
    "test_case/添加收货地址.json",
    "test_case/查询收货地址列表.json",
    "test_case/提交订单.json"
]


@pytest.mark.parametrize("file_path",file_list)
def test_login(file_path):
    SendRequest().send_request(file_path)
    pass