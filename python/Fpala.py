rev=""
s=input("enter a string:")
for i in s:
    rev=i+rev
if(s==rev):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")