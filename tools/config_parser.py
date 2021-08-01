#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: config_parse.py
# 创建时间: 2021/8/1 13:39

import configparser

import os

# 实例化configparser
import sys

from tools import log

config = configparser.ConfigParser()
# 获取配置文件位置
config_path = os.path.join(os.path.dirname(__file__), "..", "config.ini")
# 读取config.ini文件
config.read(config_path, encoding="utf-8")


class ParserConfig():

    def __init__(self):
        """
        获取当前环境
        """
        self.env = self.__get_config("env", "env")
        log.info(f"当前运行环境为：{self.env}")

    def get_url(self, app):
        """
        根据应用名获取url配置
        :param app: 应用名
        :return:
        """
        # section = f"{self.env}_url"
        section = f"{self.env}_url"
        return self.__get_config(section, app)

    def __get_config(self, section, option):
        """
        获取某个section下option的值，如果不存在，则给出错误提示
        :param section:
        :param option:
        :return: str
        """
        # 判断setion是否存在
        if not config.has_section(section):
            log.error(f"config.ini 文件中不存在section: [{section}]")
            assert False, f"config.ini 文件中不存在section: [{section}]"
        # 判断option是否存在
        if not config.has_option(section, option):
            log.error(f"config.ini 文件section: [{section}] 中不存在option: {option}")
            assert False, f"config.ini 文件section: [{section}] 中不存在option: {option}"
        # 如果都存在，则返回对应section下option的值
        return config.get(section, option)

    def __get_items(self, section):
        """
        获取section下所有的option，并返回字典格式
        :param section:
        :return:
        """
        if config.has_section(section):
            # 获取该section下所有option及其值
            res = config.items(section)
            # 字典推导式，返回一个由option和值组成的字典
            return {o[0]: o[1] for o in res}
        else:
            log.error(f"config.ini 文件中不存在section: [{section}]")
            assert False, f"config.ini 文件中不存在section: [{section}]"

    def __get_connect_config(self, section):
        """
        根据应用名获取连接配置信息
        :return:
        """
        res = self.__get_items(section)
        if "port" in res:
            # db配置中的端口号强转成数字
            res["port"] = int(res["port"])
        return res

    def get_db(self, app):
        """
        根据应用名获取数据库配置信息
        :param app: 应用名
        :return: dict
        """
        # 拼接section
        section = f"{self.env}_{app}_db"
        return self.__get_connect_config(section)

    def get_redis(self, app):
        """
        根据应用名获取redis配置信息
        :param app:
        :return:
        """
        # 拼接section
        section = f"{self.env}_{app}_redis"
        return self.__get_connect_config(section)

    def get_mq(self, app):
        """
        根据应用名获取mq的配置信息
        :param app:
        :return:
        """
        # 拼接section
        section = f"{self.env}_{app}_mq"
        return self.__get_connect_config(section)

    def get_root_path(self):
        """
        获取json数据文件根目录
        :return:
        """
        # 获取section [base] 下root_path的值
        root_path = self.__get_config("base", "root_path")
        # 判断root_path值是否为空字符串
        if root_path == "":
            # 如果为空字符串，则返回当前项目根据目录的绝对路径
            return os.path.join(os.path.dirname(__file__), "..")
        # 如果不为空，则返回root_path的值
        return root_path


if __name__ == '__main__':
    pc = ParserConfig()
    # print(pc.get_db("mall"))
    # print(pc.get_mq("mall"))
    # print(pc.get_redis("mall"))
    print(pc.get_root_path())
    # print(pc.get_url("admin"))
