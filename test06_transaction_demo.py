"""
1).连接到数据库（host:localhost user:root password:root database:books），
并开启自动提交事务
2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
3).故意抛出一个异常（模拟代码出现异常）
4).新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）
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
sql = "insert into t_book(id, title, pub_date) values(4, '西游记', '1986-01-01');"
cursor.execute(sql)
print(cursor.rowcount)
print("-" * 200)

# 主动抛出异常
raise Exception("程序出错啦。。。。。。")

# 4).新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）
sql = "insert into t_hero(name,gender,book_id) values('孙悟空', 1, 4)"
cursor.execute(sql)
print(cursor.rowcount)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
