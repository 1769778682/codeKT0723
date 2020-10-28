from test08_dbutil import DBUtil
sql = "select * from t_book"
# sql = "insert into t_book(id, title, pub_date) values(4, '西游记', '1986-01-01');"
# sql = "update t_book set title='东游记' where title = '西游记';"
# sql = "delete from t_book where title = '东游记';"
result = DBUtil.exe_sql(sql)
print(result)