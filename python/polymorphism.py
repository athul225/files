# Method overriding
# class student:
#     def __init__(self):
#         print("student details")
# class staff(student):
#     def __init__(self):
#         print("staff")
#         super().__init__()
# std=staff()

#argument passing

class student:
    def __init__(self,stname):
        print(stname)
class staff(student):
    def __init__(self,sname,stname):
        print(sname)
        super().__init__(stname)
std=staff('athul','safeela')