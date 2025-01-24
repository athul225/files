# nonparameterized constructor
# class synnefo:
#     def __init__(self):
#         self.name=input("enter student name :")
#         self.age=int(input("enter student age :"))
#         self.place=input("enter student place :")
#     def python(self):
#         print(self.name,self.age,self.place,"- python cource")
#     def mern(self):
#         print(self.name,self.age,self.place,"- mern cource")
# std1=synnefo()
# std1.python()
# std2=synnefo()
# std2.mern()


#Parameterized constructor
class synnefo:
    def __init__(self,branch):
        self.name=input("enter student name :")
        self.age=int(input("enter student age :"))
        self.place=input("enter student place :")
        self.branch=branch
    def python(self):
        print(self.name,self.age,self.place,self.branch,"-python cource")
    def mern(self):
        print(self.name,self.age,self.place,self.branch,"-mern cource")
std1=synnefo("EKM")
std1.python()
std2=synnefo("EKM")
std2.mern()    
