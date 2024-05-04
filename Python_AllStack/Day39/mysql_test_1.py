# -*- coding : utf-8 -*-
# __author__ : "GarryZheng"
# !/usr/bin/env python3


import os,sys,time,pymysql

gy_mysql_db = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root' , passwd = '1234' , db = 'gy_test' ,charset = 'utf8')

gy_db_cursor = gy_mysql_db.cursor()

gy_db_sql = 'select gy_tb5_func_add(3,4)'



try:
    exe_result = gy_db_cursor.execute(gy_db_sql)
    #gy_mysql_db.commit()
    print("exe result = ",exe_result)
    print(gy_db_cursor.fetchone())
except Exception as e:
    print("An error is : ",e)
    gy_mysql_db.rollback()

gy_db_cursor.close()
gy_mysql_db.close()


# BEGIN
#     DECLARE sum int;
#     set sum = a1 + b1;
#     RETURN sum;
# END
