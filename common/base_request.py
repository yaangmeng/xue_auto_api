#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 作者: xuepl
# 文件名: base_request.py
# 创建时间: 2021/7/5 9:05
# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_request.py
# Time       ：2021/4/2 8:45
# Author     ：xuepl
# version    ：python 3.7
"""
import json as js
import os

from common.json_data import JsonData
from tools import log


class BaseRequest():

    def __init__(self, json_str):
        json_dict = js.loads(json_str)
        self.__url = json_dict.get("url", None)  # 获取json文件中的url  /api/v1/user/login
        self.__method = json_dict.get("method", None)
        self.__headers = json_dict.get("headers", None)
        self.__files = json_dict.get("files", None)
        self.__data = json_dict.get("data", None)
        self.__json = json_dict.get("json", None)
        self.__params = json_dict.get("params", None)

    @property
    def url(self):
        """
        统一去掉字符串最左侧的"/"
        :return:
        """
        if not self.__url:
            log.error("url不能为空")
            assert False, "url不能为空"
        return self.__url.lstrip("/")

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def method(self):
        """
        返回小写字母字符串
        :return:
        """
        if not self.__method:
            log.error("method不能为空")
            assert False, "method不能为空"
        return self.__method.lower()

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def data(self):
        """
        字典格式直接返回，字符串格式如果时键值对，返回字典，如果是非键值对，直接返回
        :return:
        """
        if isinstance(self.__data, dict):
            return self.__data
        elif isinstance(self.__data, str) and "=" in self.__data:
            return {kv.split("=")[0]: kv.split("=")[1] for kv in self.__data.split("&")}
        elif isinstance(self.__data, str):
            return self.__data
        else:
            return None

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def params(self):
        """
        字典格式直接返回，字符串格式如果时键值对，返回字典，如果是非键值对，直接返回
        :return:
        """
        if isinstance(self.__params, dict):
            return self.__params
        elif isinstance(self.__params, str) and "=" in self.__params:
            return {kv.split("=")[0]: kv.split("=")[1] for kv in self.__params.split("&")}
        else:
            return None

    @params.setter
    def params(self, value):
        self.__params = value

    @property
    def headers(self):
        """
        如果是字典格式，直接返回。如果是字符串格式，转成字典格式后再返回
        :return:
        """
        if isinstance(self.__headers, str):
            return {kv.split(":")[0].strip(): kv.split(":")[1].strip() for kv in self.__headers.split("\n") if
                    ":" in kv}
        return self.__headers

    @headers.setter
    def headers(self, value):
        self.__headers = value

    @property
    def json(self):
        """
        如果是字典格式直接返回，如果是字符串格式，转成字典格式之后再返回
        :return:
        """
        if isinstance(self.__json, str):
            try:
                return js.loads(self.__json)
            except Exception as e:
                log.error("json格式不正确，{}".format(e))
                assert False, "json格式不正确，{}".format(e)
        return self.__json

    @json.setter
    def json(self, value):
        self.__json = value

    @property
    def files(self):
        """
        如果文件路径不存在，则返回一个空值。如果文件路径存在，使用rb模式打开文件，替换原来的路径再返回
        :return:
        """
        if isinstance(self.__files, dict):
            for k, v in self.__files.items():
                if os.path.isfile(v):
                    self.__files[k] = open(v, 'rb')
                else:
                    log.error("文件：{}不存在".format(v))
                    assert False, "文件：{}不存在".format(v)
        return self.__files

    @files.setter
    def files(self, value):
        self.__files = value

    def __str__(self):
        # 如果请求方法为None，则返回空字符串
        request_method = self.method if self.method else ""
        # 如果请求接口地址为None，则返回空字符串
        request_url = self.url if self.url else ""
        # 如果params关键字不为空，则返回键值对字符串
        request_params = "&".join([k + "=" + v for k, v in self.params.items()]) if self.params else None
        # 如果request_params则拼接到url中
        request_url = (request_url + "?" + request_params) if request_params else request_url
        # 不为空赋值给request_body
        print(self.json)
        request_body = self.json or (
            "&".join([k + "=" + str(v) for k, v in self.data.items()]) if self.data and isinstance(self.data,
                                                                                                   dict) else self.data) or self.__files
        # 如果request_body为空，则赋值为空字符串
        request_body = request_body if request_body else ""
        # 把请求头字典转化为字符串
        request_headers = "\n".join(
            [k + ": " + v + "\n" for k, v in self.headers.items()]) if self.headers else ""
        # 字符串格式化
        return """{} {}
{}

{}""".format(request_method, request_url, request_headers, request_body)


if __name__ == '__main__':
    b = BaseRequest()
    b.url = "/login/"
    b.method = "get"
    b.params = "name=小明&age=18"
    # b.data = "name=小明&age=18"
    # b.data = {"name": "小明", "age": 18}
    # b.data = 'adfasfsfsf'
    b.json = {"name": "小明", "age": 18}
    print(b)
