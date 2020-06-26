#作者    ：YCKJ1130   

#创建时间：2020/6/22 16:57  

#文件    ：do_mysql.py

#编译器  ：PyCharm

import pymysql
from common.read_config import ReadConfig
from common.read_path import *
class DoMysql:
    @classmethod
    def cnn_db(cls,sql):
        ReadConfig().read_config(config_path, 'DB', 'db_config')
        #数据库配置
        db_config=eval(ReadConfig().read_config(config_path, 'DB', 'db_config'))
        #创建一个数据库连接
        cnn=pymysql.Connect(**db_config)
        #创建游标
        cursor=cnn.cursor()
        #写一个sql语句----字符串
        qurey_sql=sql
        #执行语句
        cursor.execute(qurey_sql)
        #获取结果 打印结果
        res=cursor.fetchone()    #结果为一个元组
        # res1=cursor.fetchall()     #结果为包含多个元组的元组
        #关闭游标
        cursor.close()
        return res

if __name__ == '__main__':
    res =DoMysql.cnn_db('select * from member where mobilephone=15823887943')
    print(res)