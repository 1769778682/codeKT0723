"""
1).连接到数据库（host:localhost user:root password:root database:books）
2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
3).获取查询结果的总记录数
4).获取查询结果的第一条数据
5).获取全部的查询结果
"""

# 导包
import pymysql

# 创建连接
# 1).连接到数据库（host:localhost user:root password:root database:books）
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="root",
                       database="books",
                       autocommit=True)

# 获取游标
cursor = conn.cursor()

# 执行sql
# 新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
sql = "insert into t_book(id, title, pub_date) values(4, '西游记', '1986-01-01');"
cursor.execute(sql)

# 3).获取受影响的结果记录数
print("影响的结果记录数为：", cursor.rowcount)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()