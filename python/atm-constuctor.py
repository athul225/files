

class atm:
    
    def __init__ (self):
        self.balance=0
        self.pin=12345
    def deposit(self):
        self.a=int(input("enter Pin Number :"))
        if self.a==self.pin:
            self.b=int(input("eneter deposit amount :"))
            self.balance+=self.b
            print(self.balance,"is your current amount :")
        else:
            print("none") 
    def withdraw(self):
        self.b=int(input("enter Pin Number"))
        if self.a==self.pin:
            self.c=int(input("enter withdraw amount :"))
            self.balance=self.balance-self.c
            print(self.balance,"is your balance amount :")
    def balance(self):
        if self.a==self.pin:
            print(self.balance,"is your current balance :")
    def exit(self):
        if self.a==self.pin:
            print("exited")
        
num=atm()    
while True:
            print('''
                1.deposit
                2.withdraw
                3.balance
                4.exit :''',)
            choise=int(input("enter your choise :"))
            if choise==1:
                num.deposit()
            elif choise==2:
                num.withdraw()
            elif choise==3:
                num.balance()
            elif choise==4:
                num.exit()
                break
            