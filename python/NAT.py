natural=0
even=0
odd=0
for i in range(1,21):
    natural+=i
    if i%2==0:
        even+=i
    else:
        odd+=i
print("sum of natural numbers up to 20 :",natural)
print("sum of even numbers up to 20 :",even)
print("sum of odd numbers up to 20 :",odd)





rev=""
s=input("enter a string:")
for i in s:
    rev=i+rev
if(s==rev):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
    
    
    
    
upper=0
lower=0
s=input("enter a string:")
for i in s:
    print(i,'=',s.count(i))
       