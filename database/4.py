import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="Password@123",database="luminar",auth_plugin="mysql_native_password")
cursor=db.cursor()
# cursor.execute("drop table if exists car")
# sql="create table car(brand varchar(30),price int(50))"
sql1="insert into car(brand,price)values('jeep',700000)"
# sql1="delete from car where brand='mahin'"
sql2="select * from car"
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)




try:
    # cursor.execute(sql)
    # db.commit()
    cursor.execute(sql1)
    db.commit()
    cursor.execute(sql2)
    data = cursor.fetchall()


    print(data)
    db.commit()

except Exception as e:

    print(e.args)
db.close()
