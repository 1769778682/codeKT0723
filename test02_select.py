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
                       database="books")

# 获取游标
cursor = conn.cursor()

# 执行sql
# 2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
sql = "select id, title, `read`, `comment` from t_book;"
cursor.execute(sql)

# 3).获取查询结果的总记录数
print("获取的查询结果记录行数为：", cursor.rowcount)

# 4).获取查询结果的第一条数据
print(cursor.fetchone())

# 5).获取全部的查询结果
# 重置游标位置
cursor.rownumber = 0
print(cursor.fetchall())

# 关闭游标
cursor.close()

# 关闭连接
conn.close()