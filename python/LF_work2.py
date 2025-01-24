l=[]
while True:
    print('''
            1.Addition
            2.Delete 
            3.Search
            4.Exit''')
    choise=int(input("enter your choise :"))
    if choise==1:        
        n=int(input("enter no of students :"))
        for i in range(n):
           
            
            s=i+1  
            a=input("enter student name:")
            b=int(input("enter student age:"))
            c=input("enter student gender:")
            l.append([s,a,b,c])
        print(l)
    elif choise==2:
        if (l==[]):
            print("none")
        else:
            z=int(input("enter serial no :"))
            l.pop(z-1)
            print(l)
            print(z,"th details deleted")
    elif choise==3:
        if (l==[]):
            print("none")
        else:
            z=int(input("enter serial no :"))
            print(l[z-1])
    elif choise==4:
         print("exit")
         break
        
        
        
        