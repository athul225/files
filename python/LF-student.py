n=int(input("enter number of students :"))
l=[]
for i in range(n):
    name=input("enter name :")
    l.append(name)
for i in l:
    print(i[::-1],end=" ")
print()