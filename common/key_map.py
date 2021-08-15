#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: key_map.py
# 创建时间: 2021/8/8 14:49
from tools.data_tools import get_phone_number, get_string, get_random_int
from tools.response_tools import json_axtractor
from tools.vars_tools import get_var

key_map = {
    "PHONE": [get_phone_number, "随机生成手机号 用法示例：$__PHONE()$"],
    "RANDOM_STRING": [get_string, "随机生成指定长度字符串 用法示例：$__RANDOM_STRING(字符范围,字符串长度)$"],
    "RANDOM_INT": [get_random_int, "随机生成整数 用法示例：$__RANDOM_INT(最小值,最大值)$"],
    "JSON_EXTRACTOR": [json_axtractor,
                       "json提取器，根据jsonpath提取响应正文中的数据 用法示例：$__JSON_EXTRACTOR(变量名,jsonpath,匹配结果中的第几个,默认值)$"],

    "GET_VAR": [get_var, "随机生成整数 用法示例：$__GET_VAR(变量名)$"]
}
