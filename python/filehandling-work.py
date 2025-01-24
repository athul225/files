a=input("enter new filename :")
try:
    f=open(f"files/python/{a}",'x')
except:
    pass
f=open(f"files/python/{a}",'w')
n=int(input("enter number of students :"))
for i in range(n):
    b=input("enter students name :")
    f.write(b+'\n')
f=open('files/images/{a}','r')
a=f.read()
print(a)

    