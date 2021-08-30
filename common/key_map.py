#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: key_map.py
# 创建时间: 2021/8/8 14:49
from tools.assert_tools import assert_json
from tools.data_tools import get_phone_number, get_string, get_random_int
from tools.md5 import md5_passwd
from tools.mysql_tools import mysql_db
from tools.response_tools import json_axtractor
from tools.vars_tools import get_var, set_var

key_map = {
    "PHONE": [get_phone_number, "随机生成手机号 用法示例：$__PHONE()$"],
    "RANDOM_STRING": [get_string, "随机生成指定长度字符串 用法示例：$__RANDOM_STRING(字符范围,字符串长度)$"],
    "RANDOM_INT": [get_random_int, "随机生成整数 用法示例：$__RANDOM_INT(最小值,最大值)$"],
    "JSON_EXTRACTOR": [json_axtractor,
                       "json提取器，根据jsonpath提取响应正文中的数据 用法示例：$__JSON_EXTRACTOR(变量名,jsonpath,匹配结果中的第几个,默认值)$"],

    "GET_VAR": [get_var, "根据变量名获取数据 用法示例：$__GET_VAR(变量名)$"],
    "MYSQL_DB": [mysql_db, "执行sql语句关键字，sql语句必须以英文分号结尾 用法示例：$__MYSQL_DB(sql,变量名,应用名)$"],
    "ASSERT_JSON": [assert_json, "根据json预期结果判断响应正文中数据的正确性 用法示例：$__ASSERT_JSON(预期结果json)$"],
    "SET_VAR": [set_var, "把变量值存入指定变量中 用法示例：$__SET_VAR(变量名,变量值)$"],
    "MD5_PASSWD":[md5_passwd,"将密码转换成MD5 用法示例:$__MD5_PASSWD(需要转换的值)$"]
}
