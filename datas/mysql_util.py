'''

数据库操作封装类
'''
'''
1.链接数据库
2.编写sql
3.建立游标
4.运行sql,拿到返回
'''
import pymysql
from  common.config import Readconfig

class MysqlUtil:
    #第一步
    def __init__(self):
        #建立数据库链接
        config = Readconfig()
        # 获取配置文件中数据库的配置
        host=config.get(section='mysql',option='host')
        port =int(config.get(section='mysql',option='port'))
        user=config.get(section='mysql',option='user')
        password = config.get(section='mysql',option='password')
        try:
            self.mysql=pymysql.connect(host=host,user = user,password=password,database='future',port=port,charset='utf8')
        except Exception as e:
            print("连接数据库失败，host:{},port:{},user:{},password:{}".format(host, port, user, password))
            raise e

    #第三步建立游标
    def fetch_one(self,slq_str):
        '''查询一条数据并且返回'''
        cursor = self.mysql.cursor()#建立游标，返回游标实例
        cursor.execute(slq_str)#根据sql进行查询
        return cursor.fetchone()#返回一条数据
if __name__ == '__main__':
    #第二步
    sql = 'SELECT * FROM future.member ORDER BY MobilePhone LIMIT 1'

    mysql_set = MysqlUtil().fetch_one(sql)
   # a = mysql.fetch_one(sql)
    # 数据库查询后返回的对象 是元组 所以 不能get


    print(mysql_set[3])
    print(mysql_set[1])