n=int(input("enter a no:"))
for i in range(n):
    b=n%10
    n=n//10
    if(b!=0):
       print(b,end=" ")