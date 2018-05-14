import pymysql
pymysql.install_as_MySQLdb()

DB = 'user'
USER = 'root'
PASSWORD =  '8844248'

conn = pymysql.connect(db=DB,user=USER,password=PASSWORD)
conn.query("Create table user(ID varchar(50),Name varchar(200))")
conn.commit()
conn.close()