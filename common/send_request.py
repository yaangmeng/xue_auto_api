#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: SendRequest.py
# 创建时间: 2021/8/8 13:16
import json

from common.base_request import BaseRequest
from common.base_send_request import BaseSendRequest
from common.json_data import JsonData
from common.key_driver import KeyDriver


class SendRequest(BaseSendRequest):  # 继承父类BaseSendRequest
    local_vars = {}  # 类变量字典，接口串联时数据中转

    def send_request(self, file_path):
        jd = JsonData(file_path)  # 根据json文件路径解析json文件数据
        service = jd.service  # 获取service
        base_url = jd.config.get_url(service)  # 根据service获取config.ini文件中对应的base_url
        json_str = json.dumps(jd.request, ensure_ascii=False)  # 把python字典转为json字符串
        # 第一步、发送请求之前，运行关键字列表

        # 第二步、发送请求
        json_str = KeyDriver(json_str).excute_keys()  # 使用封装好的执行关键字的代码，替换请求数据中的关键字
        br = BaseRequest(json_str)  # 根据JsonData 对象 初始化一个BaseRequest对象
        br.url = base_url + '/' + br.url
        response = super().send_request(br)  # 调用父类的send_request方法，根据BaseRequest对象实现请求发送
        # 第三步、收到响应之后，执行关键字列表
        return response
