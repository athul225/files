#fn with position arguments
def display(name,age):
    print(name,age)
display('manu',22)

#fn with keyword arguments
def display(name,age):
    print(name,age)
display(age=22,name='manu')

#fn with arbitatory arguments
def display(*arg):
    print(arg)
display('manu',22,'python')
display('sunil',34)

#fn with default parameter value
def display(name,age,cource='python'):
    print(name,age,cource)
display('manu',22,'mern')
display('sunil',32)

#fn with arbitory keyword arguments
def display(**arg):
    print(arg)
display(name='manu',age=22,cource='python')
display(name='sanu',age=23,cource='mern')

