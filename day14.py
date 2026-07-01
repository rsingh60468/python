# class Student:
#     name = "ravi singh"

# s1 = Student()
# print(s1.name)

# class Cars:
#     colour = "blue"
#     brand = "BMW"

# car1 = Cars()
# print(car1.colour)
# print(car1.brand)

class Student:
    age = 20
    #DEFAULT CONSTRUCTOR
    def __init__(self):
        pass

    #PARAMETEERIZED CONSTRUCTOR
    def __init__(self, fullname):
        self.name = fullname
        self.age += 1
        print("adding new student to database..")

s1 = Student("ravi")
print(s1.name)
print(s1.age)

s2 = Student("neel")
print(s2.name)
print(s2.age)