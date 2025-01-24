#sum of 2 nos using fumctiom
def add(a,b):
    print(a+b)
add(1,2)
    
#sum of 2 nos using lambda
add=lambda a,b:a+b
print(add(1,2))

#map
def cube(num):
    return num**3
print(list(map(cube,[1,2,3,4])))

#filter
def positive(num):
    return True if num>0 else False
print(list(filter(positive,[1,-2,3,-4])))

#reduce function
from functools import reduce
def sum(x,y):
    return x+y
print(reduce(sum,[1,2,3,4]))