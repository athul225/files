import sqlite3
con=sqlite3.connect('/home/synnefo/athul/files/python/database/sql.db')
try: 
    con.execute('create table user(id int,name text,salary int)')
except:
    pass

con.execute('insert into user values(1002,"amal",500000)')
con.commit()
id=int(input("Enter Employe ID Number :"))
name=input("Enter Employe Name :")
salary=int(input("Enter Employe Salary :"))
con.execute('insert into user values(?,?,?)',(id,name,salary))
con.commit()
con.execute('update user set name="MANU" where id="1002"')
con.commit()
id=int(input("Enter update Employe ID Number :"))
name=input("Enter update Employe Name :")
# salary=int(input("Enter  Employe Salary :"))
con.execute('update user set name=(?) where id=(?)',(name,id))
con.commit()
con.execute('delete from user where id="1005"')
con.commit()
data=con.execute('select * from user')
# for i in data:
#     print(i)
for i in data:
    print("{:<20}{:<20}{:<20}".format(i[0],i[1],i[2]))
con.execute('insert into user values(1002,"amal",500000)')
con.commit()
con.execute('insert into user values(1003,"akhil",500000)')
con.commit()
con.execute('insert into user values(1004,"athul",500000)')
con.commit()
data1=con.execute('select name from user where id="1002"')
for i in data1:
    print(i)