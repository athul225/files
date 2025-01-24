# 1. single inheritence

# class synnefo:
#     def python(self):
#         print('python')
# class novavi(synnefo):
#     def staff(self):
#         print('staff')
# staff=novavi()
# staff.python()
# staff.staff()

#2. Multiple Inheritence

# class synnefo:
#     def python(self):
#         print('python')
# class novavi:
#     def webdev(self):
#         print('webdev')
# class staff(synnefo,novavi):
#     def emp(self):
#         print('emp')
# st1=staff()
# st1.python()
# st1.webdev()
# st1.emp()

# 3. multilevel inheritence

# class synnefo:
#     def python(self):
#         print('pyhton')
# class novavi(synnefo):
#     def webdev(self):
#         print('web developer')
# class staff(novavi):
#     def emp(self):
#         print('employee')
# obj=staff()
# obj.python()
# obj.webdev()
# obj.emp()

# obj2=novavi()
# obj2.python()
# obj2.webdev()

# 4. hierarchial inheritance

class metro:
    def travel(self):
        print('travel both')
class road_metro(metro):
    def road(self):
        print('travel road')
class water_metro(metro):
    def water(self):
        print('travel water')
person=road_metro()
person.road()
person.travel()
person2=water_metro()
person2.water()
person2.travel()