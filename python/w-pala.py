rev=""
i=""
s=input("enter a string:")
while(i==s):
    rev=i+rev
    if(s==rev):
        print("is a palindrome")
    else:
        print("is not a palindrome")