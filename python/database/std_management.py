import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='athul225',
    password='athul123',
    database='manage'
)
mycursor=mydb.cursor()
try:
    mycursor.execute('create database manage')
except:
    pass
try:
    mycursor.execute('create table student(id int,name text,class int)')
    mydb.commit()
except:
    pass
while True:
    choise=int(input('''
                     1.Add student
                     2.Delete Student
                     3.Update Student
                     4.Search Student
                     5.Exit
                     enter your choise: '''))
    if choise==1:
        n=int(input("enter Number of students: "))
        for i in range(n):
            id=int(input("enter the id: "))
            name=input("enter the name: ")
            age=int(input("enter the age: "))
            qry='insert into student values(%s,%s,%s)'
            val=(id,name,age)
            print("student details added successfully")
            mycursor.execute(qry,val)
            mydb.commit()
    if choise==2:
        id=int(input("enter the student id: "))
        data='delete from student where id=%s'
        data1=(id,)
        print("student details deleted  successfully")
        mycursor.execute(data,data1)
        mydb.commit()
    if choise==3:
        new_class=int(input("enter student new class: "))
        a1='update student set class=%s where id=%s'
        a2=(new_class,id)
        print("student details upadted successfully")
        mycursor.execute(a1,a2)
        mydb.commit()
    # if choise==4:
        
        
        
        