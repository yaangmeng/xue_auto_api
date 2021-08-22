#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# 作者: xuepl
# 文件名: mysql_tools.py
# 创建时间: 2021/8/15 13:54
import pymysql


class PyMySQL():

    def __init__(self, host, port, user, password, database, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def connect(self):
        # 建立数据库链接
        self.db = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password,
                                  database=self.database, charset=self.charset,
                                  cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        self.cursor = self.db.cursor()

    def excute(self, sql):
        self.connect()  # 连接数据库
        self.cursor.execute(sql)  # 执行sql语句
        # 使用fetall()获取全部数据
        data = self.cursor.fetchall()
        self.db.commit()
        # 关闭数据库
        self.close()
        return data

    def close(self):
        self.cursor.close()  # 关闭游标
        self.db.close()  # 关闭数据库连接


def mysql_db(send_request, *args):
    """
    执行sql语句，并把执行结果存入变量var_name中
    :param send_request:
    :param sql: sql语句,要求必须以英文分号结尾
    :param var_name: 变量名，如果变量名为None，则不存储
    :param app: 应用名，如果给了，就用指定的应用名的连接，如果没给，就默认用当前json文件中指定的
    :return:
    """
    sql = ""
    var_name = None
    app = ""
    flag = 0
    for i in range(len(args)):
        if ";" in args[i]:
            sql = ",".join(args[:i + 1])
            flag = 1
        elif flag == 1:
            var_name = args[i]
            flag += 1
        elif flag == 2:
            app = args[i]
            flag += 1
        else:
            pass

    if app == "":  # 判断应用名是否为空
        app = send_request.jd.service  # 若为空，则使用json文件中service的值
    db = PyMySQL(**send_request.jd.config.get_db(app))  # 实例化PyMySQL对象，**字典拆包语法
    res = db.excute(sql)
    if var_name is not None:
        send_request.local_vars[var_name] = res


if __name__ == '__main__':
    db = PyMySQL("api.xuepl.com.cn", 3306, "root", "SongLin2021", "mall")
    res = db.excute("update tb_newbee_mall_user set is_deleted = 1 where user_id = 58;")
    print(res)
    res = db.excute("select * from tb_newbee_mall_user where user_id = 58;")
    print(res)
