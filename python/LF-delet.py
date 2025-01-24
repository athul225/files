
l=[1,2,2,3,4,5,6,7,7]
r=[]
for i in l:
    count=0
    for j in range(len(l)):
        if i==l[j]:
            count=count+1
    if count==1:
        r.append(i)        
print(r)
