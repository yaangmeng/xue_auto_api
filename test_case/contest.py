# -*- coding:utf-8 -*-
"""
@author:yangmeng
@file: contest.py
@date: 2021/08/22 15:06
#@Software : PyCharm

"""
def pytest_collection_modifyitems(session, config, items):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")