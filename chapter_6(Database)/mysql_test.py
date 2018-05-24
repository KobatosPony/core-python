import pymysql
pymysql.install_as_MySQLdb()

HOST = 'localhost'
PORT = '3306'
DB = 'user'
USER = 'root'
PASSWORD = '8844248'

conn = pymysql.connect(db=DB,user=USER,password=PASSWORD)
conn.query("Create table user(ID varchar(50),Name varchar(200))")
conn.commit()

# 创建游标
cu = conn.cursor()
cu.execute("select * from user")

conn.close()