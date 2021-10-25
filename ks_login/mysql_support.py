import pymysql
import uuid
import time
from datetime import datetime

class MysqlDataGet(object):


    def write_log(self, log_title, log_level, log_category, log_data):
        try:
            if isinstance(log_title, str):
                pass
            else:
                log_title = str(log_title)
        except Exception as e:
            print(e)
        # 取项目配置文件参数
        host = '192.168.254.3'
        user = 'root'
        password = '123456'
        db_name = 'mysql_support'
        port = '3306'
        # 打开数据库连接
        db = pymysql.connect(host=host, user=user, password=password, db=db_name, port=int(port),  charset='utf8')
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql_insert = """insert into log_data_logmodel(log_id, log_title,log_level, log_category, log_data, created_time) 
                        values(%s,%s,%s,%s,%s,%s)"""
        try:
            log_id = str(uuid.uuid4())
            cur.execute(sql_insert, (log_id, log_title, log_level, log_category, log_data, datetime.now()))  # 执行sql语句
            db.commit()
        except Exception as e:
            print(str(e))
        finally:
            db.close()