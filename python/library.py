l=[]
while True:
    print('''
            1.Add
            2.Remove
            3.Update
            4.View
            5.Search
            6.Exit''')
    choise=int(input("enter your choise :"))
    if choise==1:
        n=int(input("enter no of books :"))
        for i in range(n):
           
            
            s=i+1  
            a=input(" enter Book Name:")
            b=input(" enter Author of Book:")
            c=int(input(" enter Book Published Year:"))
            l.append([s,a,b,c])
        print(l)
    elif choise==2:
        if (l==[]):
            print("none")
        else:
            d=int(input("enter serial no of the Book:"))
            l.pop(d-1)
            print(l)
            print(d,"th book deleted")
    elif choise==3:
        if (l==[]):
            print("none")
        else:
            a=input(" enter Serial Number of Book :")
            print(l[d-1])
    elif choise==4:
        print(l)
    elif choise==5:
        if (l==[]):
            print("none")
        else:
            d=int(input("enter serial no :"))
            print(l[d-1])
    elif choise==6:
          print("Exit")     
          break 
            
        
        
        
            
        
        
    
    
        