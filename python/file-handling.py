try:
    f=open('files/images/module.txt','x')
except:
    pass
f=open('files/images/module.txt','w')
f.write('welcome to the home')
f=open('files/images/module.txt','r')
a=f.read(3)
b=f.read()
print(a)
