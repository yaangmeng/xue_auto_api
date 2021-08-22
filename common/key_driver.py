#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: key_driver.py
# 创建时间: 2021/8/8 13:40
import re

from common.key_map import key_map


class KeyDriver():
    def __init__(self, data):
        self.__data = data

    def __get_keys_list(self, data):
        start = -1
        length = len(data)
        flag = 0
        keys = []  # 存储关键字
        for i in range(length):  # 获取字符串中每个字符的下标
            # print(data[i])  # 根据下标打印出字符串中的字符
            if data[i] == "$":
                if i + 3 < length and data[i + 1:i + 3] == "__":
                    flag -= 1
                    if start == -1:
                        start = i
                elif i != 0 and data[i - 1] == ")":
                    flag += 1
                    if flag == 0:
                        key = data[start:i + 1]
                        keys.append(key)
                        start = -1
        return keys

    @property
    def keys(self):
        return self.__get_keys_list(self.__data)

    def __get_key_name(self, key):
        r = re.compile(r"^(.*?)\(")
        res = r.findall(key)
        if len(res) != 0 and res[0] != "":
            return res[0]
        return None

    def __get_key_args(self, key):
        r = re.compile(r"\((.*?)\)")
        res = r.findall(key)
        if len(res) != 0 and res[0] != "":
            args_list = res[0].split(",")
            args_list = [k.strip() for k in args_list]
            return args_list
        return []

    def __replace_key(self, data, key, res):
        """
        使用关键字方法运行结果替换掉原字符串中的关键字
        :param data: 原字符串
        :param key: 关键字
        :param res: 关键字方法运行结果
        :return:
        """
        if res is None:  # 判断res是否为空
            return data  # 如果为空，直接返回原字符串
        return data.replace(key, str(res))  # 如果不为空，则使用关键字方法运行结果，替换调原字符串中的关键字

    def __excute_keys(self, send_request, key):
        """
        执行嵌套关键字  $__PHONE($__PHONE()$)$
        :param key:关键字
        :return:
        """
        key = key[3:-1]  # PHONE($__PHONE()$)
        if "$__" in key:  # 判断$__是否在关键字中出现，如果出现，则说明有关键字嵌套的问题
            keys = self.__get_keys_list(key)  # 获取关键字中的嵌套关键字
            for k in keys:
                res = self.__excute_keys(send_request, k)  # 递归调用关键字执行方法
                key = self.__replace_key(key, k, res)  # 使用关键字执行结果，替换掉原关键字中的嵌套关键字
        key_name = self.__get_key_name(key)
        key_args = self.__get_key_args(key)
        func_name = key_map[key_name][0]
        res = func_name(send_request, *key_args)  # 列表拆包语法
        return res

    def excute_keys(self, send_request):
        keys = self.keys
        for k in keys:
            # key_name = self.__get_key_name(k)
            # key_args = self.__get_key_args(k)
            # func_name = key_map[key_name][0]
            # func_name = key_map[key_name][0]
            # res = func_name(*key_args)  # 列表拆包语法
            res = self.__excute_keys(send_request, k)
            self.__data = self.__replace_key(self.__data, k, res)
        return self.__data


if __name__ == '__main__':
    print(KeyDriver("name: $__RANDOM_STRING(abcdefghigklmnopqrstuvwxyz,$__RANDOM_INT(6,12)$)$").excute_keys())
