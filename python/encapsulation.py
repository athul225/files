class vehicle:
    def __init__(self,brand):
        self.__brand=brand
    def displaybrand(self):
        return f"the brand is{self.__brand}"
    def brand(self):
        return self.displaybrand()
   
car=vehicle(" mastang")
# print(car.__brand)
print(car.brand())