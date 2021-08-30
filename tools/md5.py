# -*- coding:utf-8 -*-
"""
@author:yangmeng
@file: md5.py
@date: 2021/08/29 13:14
#@Software : PyCharm

"""
import hashlib

def md5_passwd(send_request,mess):
    abss=str(mess)
    md = hashlib.md5()  # 构造一个md5对象
    md.update(abss.encode())
    res = md.hexdigest()
    return str(res)

if __name__ == '__main__':
    print(md5_passwd(123456))