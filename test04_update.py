"""
1).连接到数据库（host:localhost user:root password:root database:books autocommit:True）
2).更新[西游记]图书名称为（title:东游记）
"""

# 导包
import pymysql

# 创建连接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="root",
                       database="books",
                       autocommit=True)

# 获取游标
cursor = conn.cursor()

# 执行sql
sql = "update t_book set title='东游记' where title = '西游记';"
cursor.execute(sql)
print(cursor.rowcount)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()