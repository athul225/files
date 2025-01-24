a=input("enter new filename :")
try:
    f=open(f"files/python/{a}",'x')
except:
    pass
f=open(f"files/python/{a}",'w')
n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(1,11):
        c=(f"{i} x {j} = {i*j}")
        f.write(c+'\n')
    f.write('\n')