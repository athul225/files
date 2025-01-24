a=input("enter new filename :")
try:
    f=open(f"files/python/{a}",'x')
except:
    pass
f=open(f"files/python/{a}",'w')
n=int(input("enter number of students :"))
for i in range(n):
    b=input("enter students name :")
    c=b[::-1]
    f.write(b+'\n')
f=open(f'files/python/{a}','r')
c=f.read()
print(c)