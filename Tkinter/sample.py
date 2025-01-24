import tkinter

win=tkinter.Tk()

def data():
    text1=e1.get()
    print(text1)
    l2.config(text=text1)
    l2.pack()
    
win.title('synnefo')
win.geometry('200x150')
win.minsize(100,100)
win.maxsize(500,500)
win.config(background='blue')
l1=tkinter.Label(win,text='WELCOME TO ALL')
l1.pack()
# l1.grid(row=0,colum=0)
e1=tkinter.Entry(win,background='black',foreground='white')
e1.pack()
b1=tkinter.Button(win,text='submit',command=data)
b1.pack()
l2=tkinter.Label(win)
win.mainloop()