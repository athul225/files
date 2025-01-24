class calculator:
    
    def __init__ (calc):
        while True:
            choise=(input('''
                1.Addition
                2.subtraction
                3.Division
                4.Multiplication :''',))
            a=int(input("enter a number :"))
            b=int(input("enter a number :"))
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
        
    def ad(calc):
        print(calc.add,)
    def sub(calc):
        print(calc.su)
    def mul(calc):
            print(calc.mu)
    def div(calc):
        print(calc.di)
result=calculator()
result.add()  
result=calculator()
result.sub()     
result=calculator()
result.mul()       
result=calculator()
result.div()            
        