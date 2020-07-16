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
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('john','MIC',28,'9',300)"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)

db.close()