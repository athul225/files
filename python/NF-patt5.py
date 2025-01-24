# n=1
# for i in range(5):
#     for j in range(i):
#         print(n,end="    ")
#         n=n+1
#     print()



# for i in range(5):
#     for j in range(i):
#         print(j+1,end="  ")
#     print()


# for i in range(4):
#     for j in range(i+1):
#         print(i+1,end="  ")
#     print()


# for i in range(5,1,-1):
#     for j in range(i-1):
#         print(j+1,end="  ")
#     print()
    
    
# for i in range(5):
#     for j in range(3-i+1):
#         print(j+1,end="  ")
       
#     print()

n=4
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end="  ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()