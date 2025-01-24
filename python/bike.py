cost=int(input("enter the cost"))
if(cost>100000):
    print(cost*0.15,"is your tax")
elif(cost<=100000 and cost>50000):
    print(cost*0.10,"is your tax")
else:
    print(cost*0.05,"is your tax")