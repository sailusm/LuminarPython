import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="Luminar",
    auth_plugin='mysql_native_password'


)

cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(10),LAST_NAME VARCHAR(20),AGE INT(10),SEX INT(10),INCOME FLOAT(50))"""
cursor.execute(sql)
db.close()