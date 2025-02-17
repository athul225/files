import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='athul225',
    password='athul123',
    database='sample'
)
mycursor=mydb.cursor()
try:
    mycursor.execute('create database sample')
except:
    pass
try:
    mycursor.execute('create table student(id int,name text,age int)')
    mydb.commit()
except:
    pass
id=int(input("enter the id: "))
name=input("enter the name: ")
age=int(input("enter the age: "))
qry='insert into student values(%s,%s,%s)'
val=(id,name,age)
print("student details added successfully")
mycursor.execute(qry,val)
# data=mycursor.execute('delete  from student where id=(%s)')
# data1=(id,)
# mycursor.execute(data,data1)

mydb.commit()