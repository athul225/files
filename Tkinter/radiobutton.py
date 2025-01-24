import tkinter

win=tkinter.Tk()
def data2():
    text1=v1.get()
    print(text1)
    
win.title('synnefo')
win.geometry('200x150')
win.minsize(100,100)
win.maxsize(500,500)
win.config(background='blue')
v1=tkinter.IntVar()
l1=tkinter.Label(win,text='male')
l1.pack()
r1=tkinter.Radiobutton(win,variable=1,value=1)
r1.pack()
l2=tkinter.Label(win,text='female')
l2.pack()
r2=tkinter.Radiobutton(win,variable=1,value=2)
r2.pack()
b1=tkinter.Button(win,text='check',command=data2)
b1.pack()
win.mainloop()