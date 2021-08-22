#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: SendRequest.py
# 创建时间: 2021/8/8 13:16
import json

import allure

from common.base_request import BaseRequest
from common.base_send_request import BaseSendRequest
from common.json_data import JsonData
from common.key_driver import KeyDriver
from tools import log


class SendRequest(BaseSendRequest):  # 继承父类BaseSendRequest
    local_vars = {}  # 类变量字典，接口串联时数据中转

    def send_request(self, file_path):
        self.jd = JsonData(file_path)  # 根据json文件路径解析json文件数据
        service = self.jd.service  # 获取service
        base_url = self.jd.config.get_url(service)  # 根据service获取config.ini文件中对应的base_url
        json_str = json.dumps(self.jd.request, ensure_ascii=False)  # 把python字典转为json字符串

        # 调用__add_allure方法，实现allure报告集成
        self.__add_allure()
        # 第一步、发送请求之前，运行关键字列表
        for k in self.jd.pre_process:
            KeyDriver(k).excute_keys(self)  # 运行列表中的关键字

        # 第二步、发送请求
        json_str = KeyDriver(json_str).excute_keys(self)  # 使用封装好的执行关键字的代码，替换请求数据中的关键字
        br = BaseRequest(json_str)  # 根据JsonData 对象 初始化一个BaseRequest对象
        br.url = base_url + '/' + br.url
        self.response = super().send_request(br)  # 调用父类的send_request方法，根据BaseRequest对象实现请求发送
        # 请求日志
        allure.attach(f"{self.response.http_request}", "请求报文", allure.attachment_type.TEXT)
        log.debug(f"----------请求报文为-------------\n{self.response.http_request}")
        # 响应日志
        allure.attach(f"{self.response.http_response}", "响应报文",
                      allure.attachment_type.TEXT)
        log.debug(f"----------响应报文为-------------\n{self.response.http_response}")
        # 第三步、收到响应之后，执行关键字列表
        for k in self.jd.post_process:
            KeyDriver(k).excute_keys(self)  # 运行列表中的关键字
        log.debug(f"-------local_vars：{self.local_vars}")  # 日志输出local_vars 方便写用例调试
        return self.response

    def __add_allure(self):
        for k in self.jd.allure:
            getattr(allure.dynamic, k)(self.jd.allure[k])

        """
        假如说 k = "feature"
        getattr(allure.dynamic, k) 等价于 allure.dynamic.feature
        """
