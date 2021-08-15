#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 作者: xuepl
# 文件名: http_tools.py
# 创建时间: 2021/7/13 20:34
import json


def data_kv_to_dict(data):
    """
    name=小明&sex=男 转为dict
    :param data:
    :return:
    """
    d = {}
    kv = data.split("&")  # ["name=value","sex=男"]
    for i in range(len(kv)):  # i=0,1
        k, v = kv[i].split("=")  # ["name","value"] k = "name",v = "value"
        d[k] = v
    return d


def header_kv_to_dict(s):
    """
    请求头字符串转为字典
    :param s:
    :return:
    """
    d = {}
    kv = s.split("\n")  # ["name: value","sex: 男"]
    for i in range(len(kv)):  # i=0,1
        if ": " not in kv[i]:  # 判断如果 : 不在字符串中，则跳过本次循环
            continue
        k, v = kv[i].split(": ")  # ["name","value"] k = "name",v = "value"
        d[k.strip()] = v.strip()
    return d

    pass


def dcit_to_kv_header(d):
    """
    字典转为请求头字符串
    :param d:
    :return:
    """
    # {"Host":"api.xuepl.com.cn:28019", "Connection":"keep-alive" }
    l = []
    for k, v in d.items():
        l.append(k + ": " + v)
    return "\n".join(l)


def dcit_to_kv_data(d):
    """
    字典转为键值对格式字符串
    :param d:
    :return:
    """
    # {"Host":"api.xuepl.com.cn:28019", "Connection":"keep-alive" }
    if d is None:
        return None
    l = []
    for k, v in d.items():
        l.append(str(k) + "=" + str(v))
    return "&".join(l)


def get_file_name(self, d):
    """
    获取文件名
    :param self:
    :param d:
    :return:
    """
    if d is None:
        return
    for k, v in d.items():
        d[k] = v.name
    return d


def format_json(json_str):
    """
    json字符串格式化，如果是二进制格式，使用unicode编码格式解码
    :param json_str:
    :return:
    """
    if isinstance(json_str, bytes):  # 如果是二进制类型
        json_str = json_str.decode('unicode_escape')  # 使用unicode编码格式解码
    try:
        json_dict = json.loads(json_str)
    except:
        return json_str
    return json.dumps(json_dict, indent=2, ensure_ascii=False)
