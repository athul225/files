s=[]
n=int(input("enter no of student :"))
for i in range(1,n+1):
    print('Student :',i)
    d={}
    a=input("enter student name :")
    b=int(input("enter student age :"))
    c=int(input("enter student class :"))
    d['name']=a
    d['age']=b
    d['class']=c
    s.append(d)
print('Students below or equal to 12')
for i in s:
    if i['age']<=12:
        print(i)
print('Students abouve 12')
for i in s:
    if i['age']>12:
        print(i)

    
    
        
    