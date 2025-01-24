

while True:
    print('''
            1.Addition
            2.subtraction
            3.Division
            4.Multiplication
            5.Modulus''')  
    a=int(input("enter a number :"))
    b=int(input("enter a number :"))
    choise=int(input("enter your choise :"))
    
    if choise==1:
        def add():
            print(a+b)
        add()
        
    elif choise==2:
        def sub():
            print(a-b)
        sub()
        
    elif choise==3:
        def div():
            print(a/b)
        div()
        
    elif choise==4:
        def mul():
            print(a*b)
        mul()
        
    elif choise==5:
        def mod():
            print(a%b)
        mod()    
        break
    
    


