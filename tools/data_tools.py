#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: data_tool.py
# 创建时间: 2021/8/8 14:46

from faker import Faker
import random

fake = Faker("zh_CN")  # 默认英文，初始化为中文

"""
定义生成数据关键字方法，入参是字符串，出参也是字符串
"""


def get_phone_number(send_request):
    """
    随机生成手机号
    :return:
    """
    return str(fake.phone_number())


def get_string(send_request, content, length):
    """
    随机生成指，长度为length，字符在content之中选择的字符串
    :param content:
    :param length:
    :return:
    """
    if not isinstance(length, int):
        length = int(length.strip())
    return "".join(random.choices(content, k=length))


def get_random_int(send_request, start, end):
    """
    随机生成min至max之间的整数
    :param start: 最小值
    :param end: 最大值
    :return:
    """
    if not isinstance(start, int):
        start = int(start.strip())
    if not isinstance(end, int):
        end = int(end.strip())
    return str(random.randint(start, end))
