#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: vars_tools.py
# 创建时间: 2021/8/15 13:15

def get_var(send_request, var_name):
    """
    根据var_name获取send_request对象属性local_vars字典中的value
    :param send_request: send_request对象
    :param var_name: 变量名，也就是local_vars字典的key
    :return: 字符串
    """
    # 获取local_vars变量
    local_vars = send_request.local_vars
    # 返回var_name对应的value
    return local_vars[var_name]
