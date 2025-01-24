unit=int(input("enter the number electricity units consumed:"))
if(unit<=100):
    print("no charge")
elif(unit<=200):
    unit=unit-100
    print(unit*5,"is your bill")
# elif(unit>200):
#     unit=unit-200
#     print(unit*10,"is your bill")
else:
    unit=unit-200
    print(unit*10+500,"is your bill")