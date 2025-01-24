import tkinter

win=tkinter.Tk()

def data():
    win2=tkinter.Tk()
    win2.title('novavi')
    win2.geometry('200x150')
    win2.config(background='yellow')
    text=e1.get()
    print(text)
    l2=tkinter.Label(win2,text=text)
    l2.pack()
    
win.title('synnefo')
win.geometry('200x150')
# win.minsize(100,100)
# win.maxsize(500,500)
win.config(background='blue')
# l1=tkinter.Label(win,text='WELCOME TO ALL')
# l1.pack()
# l1.grid(row=0,colum=0)
e1=tkinter.Entry(win,background='black',foreground='white')
e1.pack()
b1=tkinter.Button(win,text='submit',command=data)
b1.pack()
l2=tkinter.Label(win)
win.mainloop()