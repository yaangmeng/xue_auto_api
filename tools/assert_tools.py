#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: assert_tools.py
# 创建时间: 2021/8/22 9:28
import json
from tools import log


def assert_json(send_request, *args):
    json_dict = json.loads(",".join(args))  # 断言json转为字典
    r_json = send_request.response.response.json()  # 获取响应正文（字典格式）
    compare_json(r_json, json_dict)


def compare_json(actual, expect):
    if isinstance(actual, dict) and isinstance(expect, dict):
        for k in expect:
            if k in actual:
                if isinstance(expect[k], dict) or isinstance(expect[k], list):
                    compare_json(actual[k], expect[k])
                assert_true(actual[k] == expect[k],
                            sucess=f'{json.dumps({k: expect[k]}, ensure_ascii=False)} 断言通过',
                            failed=f'预期结果: {json.dumps({k: expect[k]}, ensure_ascii=False)} != 实际结果: {json.dumps({k: actual[k]}, ensure_ascii=False)}，断言失败')
            else:
                assert_true(False, failed=f"key: {k}在响应json：{actual}中不存在")
    elif isinstance(expect, list) and isinstance(actual, list):
        length = len(expect)
        for i in range(length):
            if i < len(actual):
                if isinstance(expect[i], dict) or isinstance(expect[i], list):
                    compare_json(actual[i], expect[i])
                assert_true(expect[i] in actual, sucess=f'{expect[i]}存在于列表{actual},断言通过',
                            failed=f'列表{actual}不存在{expect[i]},断言失败')


def assert_true(result, failed="", sucess=""):
    if result:
        log.info(sucess)
    else:
        log.error(failed)
        assert result, failed


if __name__ == '__main__':
    assert_json(None, '{"resultCode": 200', '"message":"登录失败"}')
