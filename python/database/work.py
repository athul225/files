import tkinter
win=tkinter.Tk()


import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='athul225',
    password='athul123',
    database='page'
 
)
mycursor=mydb.cursor()
try:
    mycursor.execute('create database page')
except:
    pass
try:
    mycursor.execute('create table student(name text,age int,email text)')
    mydb.commit()
except:
    pass


def data():
    text1=e1.get()
    text2=e2.get()
    text3=e3.get()
    qry='insert into student values(%s,%s,%s)'
    val=(text1,text2,text3)
    add=mycursor.execute(qry,val)
    mydb.commit()
    print(add)
    print(text1,text2,text3)
 
def data2():
    win1=tkinter.Tk()
    win1.title("view all")
    win1.geometry("200x150")
    win1.config(background="blue")
    all=mycursor.execute('select * from student')
    all=mycursor.fetchone()
    if all:
        for i in all:
            print(i)   
win.title('page')
win.geometry('200x150')
win.maxsize(800,800)
win.config(background='white')
e1=tkinter.Entry(win,background='black',foreground='white')
e1.pack()
e2=tkinter.Entry(win,background='black',foreground='white')
e2.pack()
e3=tkinter.Entry(win,background='black',foreground='white')
e3.pack()
b1=tkinter.Button(win,text='add',command=data)
b1.pack()
b2=tkinter.Button(win,text='view all',command=data)
b2.pack()
win.mainloop()