#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: vars_tools.py
# 创建时间: 2021/8/15 13:15
import jsonpath


def get_var(send_request, var_name):
    """
    根据var_name获取send_request对象属性local_vars字典中的value
    :param send_request: send_request对象
    :param var_name: 变量名，也就是local_vars字典的key
    :return: 字符串
    """
    path = None
    if var_name.find("[") != -1:  # 从变量名中查询[ 如果有，说明需要按照字典取值的方式走
        key = var_name[:var_name.find("[")]  # 先获取key
        path = f'${var_name[var_name.find("["):]}'  # 再获取jsonpath
    else:
        key = var_name
    # 获取local_vars变量
    local_vars = send_request.local_vars
    # 返回var_name对应的value
    if key not in local_vars:  # 判断变量名是否再local_vars中，如果不在，直接返回
        return
    value = local_vars[key]
    if path:
        path = path.replace("'", '"')
        path = path.replace('["', '.')
        path = path.replace('"]', '')
        res = jsonpath.jsonpath(value, path)  # 使用jsonpath提取字典中的数据
        if res:  # 如果res不为False
            value = res[0]  # 把jsonpath提取到的数据赋值给value
    return value


def set_var(send_request, var_name, value):
    send_request.local_vars[var_name] = value


if __name__ == '__main__':
    # 取出变量名中的key
    json_dict = [{'user_id': 58, 'nick_name': '13765594151', 'login_name': '13765594151',
                  'password_md5': '4cd6f5ccdc3f83d3873cb0394e02702e', 'introduce_sign': '随新所欲，蜂富多彩', 'is_deleted': 1,
                  'locked_flag': 0, 'create_time': ""}]
    path = "$[0].password_md5"
    print(jsonpath.jsonpath(json_dict, "$[0].password_md5"))
    print(jsonpath.jsonpath(json_dict, "$[0].login_name"))
