while True:
    print('''
        1.Add Money
        2.Withdraw Money
        3.Balance Checking
        4.Exit''')
    s=5000
    choise=int(input("enter your choise :"))
    
    if choise==1:
        a=int(input("Enter Amount :"))
        def add():
            print(s+a,"is your Current Amount")
        add()
    elif choise==2:
        b=int(input("Enter withdraw amount :"))
        c=(s+a)-b
        if c<=s:
            def witdraw():
                print(b,"Amount is Withdrawed")
           
                print(c,"is your Current Amount")
            witdraw()
        else:
            print("not")
    elif choise==3:
        def balance():
            print(s+a,"is your current balance")
        balance()
    elif choise==4:
        def exit():
            print("Exit")
        exit()
    else:
        print("")
            
        
        
        