#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: response_tools.py
# 创建时间: 2021/8/15 10:02


# jsonpath
import random

import jsonpath


def json_axtractor(send_request, var_name, json_path, match_no="0", default=None):  # 定义所有关键字方法中，入参都是字符串
    """
    提取响应字典中的数据
    :param send_request: send_request对象
    :param var_name: 字典的key，也可以说是变量
    :param json_path: jsonpath
    :param match_no: 0表示随机获取一个值，1 表示获取第一个数据，2表示获取第二个数据.....
    :param default: 提取不到值的时候，设置一个默认值
    :return:
    """

    if not hasattr(send_request, "response"):  # 判断send_request对象中，是否有response属性
        return
    # 获取响应字典
    response = send_request.response.response.json()
    # 对jsonpath做一个预处理操作，转为jsonpath模块支持的类型
    json_path = json_path.replace("'", '"')  # 把json_path中所有的单引号，都替换成双引号
    json_path = json_path.replace('["', ".")  # 把json_path中所有的["，都替换成.
    json_path = json_path.replace('"]', "")  # 把json_path中所有的"]，都替换成空字符串
    # 根据jsonpath获取响应字典中的数据
    res = jsonpath.jsonpath(response, json_path)
    # value, 随机取一个，还是指定一个
    value = default
    if res:
        match_no = int(match_no)  # 把字符串match_no转换为数字match_no
        if match_no > 0:
            value = res[match_no - 1]  # 第一个数据下标为0
        else:
            value = random.choice(res)
    # 把获取到的数据，存入local_vars字典中
    if value:
        send_request.local_vars[var_name] = value  # 变量名（字典的key）
