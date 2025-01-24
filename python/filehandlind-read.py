try:
    f=open('files/python/read.txt','x')
except:
    pass
f=open('files/python/read.txt','r')
# a=f.readline(3)
# b=f.readline()
# print(a)
# print(b)

# a=f.readlines()
# b=f.readlines()
# print(a)
# print(b)

upper=0
lower=0
s=0
a=f.readlines()
print(a)
for i in a:
    b=0
    b=b+1
    for j in i:
        if j.isupper():
            upper=upper+1
        elif j.islower():
            lower=lower+1
        s=s+1
s=s-b
print(upper)
print(lower)
print(s)
    