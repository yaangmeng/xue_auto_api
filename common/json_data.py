#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: json_data.py
# 创建时间: 2021/8/8 9:46
import json
import os

from tools import log


class JsonData():

    def __init__(self, file_path):
        file_path = self.__get_json_file(file_path)
        self.__read_json(file_path)
        pass

    def __get_json_file(self, file_path):
        """
        根据config_parser.py 中get_root_path来拼接json文件的路径
        get_root_path：如果config.ini root_path中有值，则返回该值。如果为空，则返回当前项目根目录的绝对路径

        :param file_path:
        :return:
        """
        pc = self.config
        root_path = pc.get_root_path()  # 获取json文件根目录
        file_path = os.path.join(root_path, file_path)  # 把root_path 和file_path拼接成一个全新的路径
        if os.path.isfile(file_path) and file_path.endswith(".json"):  # 判断文件是否存在,并且该文件是以.json结尾
            return file_path
        log.error(f"json文件{file_path}不存在")  # 如果json文件不存在，则打印到日志中
        assert False, f"json文件{file_path}不存在"  # 如果json文件不存在，则停止代码运行

    def __read_json(self, file_path):
        """
        把json文件数据中的应用名信息存入__service属性中，其他字符串存入__request属性中
        :param file_path:
        :return:
        """
        with open(file_path, "r", encoding="utf-8") as f:
            json_str = f.read()
            json_dict = json.loads(json_str)  # 把json字符串，转为字典或者列表
            self.__service = json_dict.pop("service", None)  # 使用字典的get方法获取service的值，如果获取不到，则给默认值None
            self.__pre_process = json_dict.pop("pre_process", [])  # 请求发送之前的关键字列表
            self.__post_process = json_dict.pop("post_process", [])  # 请求收到响应之后的关键字列表
            self.__allure = {}
            self.__allure.update(self.__get_value(json_dict, "feature"))
            self.__allure.update(self.__get_value(json_dict, "story"))
            self.__allure.update(self.__get_value(json_dict, "title"))
            self.__request = json_dict  # 剩余的存入__request属性中

    def __get_value(self, d, key):
        """
        判断key是否再d中存在，如果在则返回对应的key和value，如果不在，则返回一个{}
        :param d:
        :param key:
        :return:
        """
        if key not in d:
            return {}
        a = {}
        a[key] = d.pop(key)
        return a

    @property
    def config(self):
        from tools.config_parser import ParserConfig  # 使用局部导入，解决模块递归导入报错的问题
        return ParserConfig()

    @property
    def service(self):
        return self.__service

    @property
    def request(self):  # 只读属性
        return self.__request

    @property
    def post_process(self):  # 只读属性
        return self.__post_process

    @property
    def pre_process(self):  # 只读属性
        return self.__pre_process

    @property
    def allure(self):  # 只读属性
        return self.__allure


if __name__ == '__main__':
    jd = JsonData("test_case/登录.json")
