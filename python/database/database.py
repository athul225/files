import sqlite3
con=sqlite3.connect('/home/synnefo/athul/files/python/database/Database.db')
try: 
    con.execute('create table user(id int,name text,salary int)')
except:
    pass
n=int(input("Enter Number Of Employees :"))
for i in range(1,n+1):
    id=int(input("Enter Employe ID Number :"))
    name=input("Enter Employe Name :")
    salary=int(input("Enter Employe Salary :"))
    con.execute('insert into user values(?,?,?)',(id,name,salary))
    con.commit()

