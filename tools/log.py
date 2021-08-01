#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: log.py
# 创建时间: 2021/8/1 13:33
import logging
import os
from logging.handlers import RotatingFileHandler

'''
封装log方法
'''
logger = logging.getLogger(__name__)  # 获取记录器对象
logger.setLevel(level=logging.DEBUG)  # 设置记录器的日志级别
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs/")  # 确定日志文件夹
if not os.path.exists(root_path):  # 如果日志文件夹不存在，创建一个
    os.makedirs(root_path)
# 创建一个按大小自动切割日志的日志处理器。 root_path + 'api.log' api日志路径，maxBytes 设置日志切割大小，单位时byte
# backupCount 设置备份文件的最大个数，encoding 设置日志文件编码格式
handler = RotatingFileHandler(root_path + 'api.log', maxBytes=1024 * 1024 * 2, backupCount=5, encoding='utf-8')
handler.setLevel(logging.DEBUG)  # 设置日志处理器的日志级别
# 创建一个日志格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)  # 日志格式化期和日志处理器绑定
logger.addHandler(handler)  # 日志处理器和日志记录器绑定

handler2 = RotatingFileHandler(root_path + 'error.log', maxBytes=1024 * 1024 * 2, backupCount=30, encoding='utf-8')
handler2.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter)
logger.addHandler(handler2)

handler3 = logging.StreamHandler()  # 创建一个日志输出到控制台的处理器
handler3.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler3.setFormatter(formatter)
logger.addHandler(handler3)


def info(msg):
    logger.info(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)
