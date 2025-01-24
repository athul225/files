l=[1,2,3,4,4]
l.append(25)
print(l)


l.append([26,27])
print(l)
print(l[6][1])

l.extend([50,60,70])
print(l)

l.insert(2,28)
print(l)

# l.clear()
# print(l)
    
l.pop()
print(l)    

l.pop(3)
print(l)

l.remove(4)
print(l)



l=[21,22,25,25,26,28]

c=l.count(25)
print(c)

c=l.index(22)
print(c)

c=l.index(25,1)
print(c)

l.sort()
print(l)

l.reverse()
print(l)

l.copy()
print(l)

l.sort()
print(l)

l.copy()
print(l)



l=[21,22,25,25,26,28]
for i in l:
    print(i,end="  ")
    