# Getters and Setters
# Why - use cases
# To hide the data - Separation of concern

# Syntax 2 functions, 1 to get information and the other to set the information

# create a class called student

# class Student:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
#
#     def getStudent(self, value):
#         self.__name # __double underscores are used to hide the data (can be: variable, or whatever has dunder in front of it
#
#     def setStudent(self, value):
#         self.__name = value
#
# student_obj = Student(name= 'Eman', company= 'Sparta')
# print(student_obj)
# print("student name: ")

class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    @property # a decorator in python is any callable python object that is used to modify a function or a class
    def student(self, value):
        self.__name # __ underscores are used to hide the data (can be: variable, or whatever has dunder infront of it

    @Student.setter
    def student(self, value):
        print("calling @student.student method")
        self.__name = value

student_obj = Student("Emmanuel", "Sparta")
print("Student name is " + student_obj.name)
print("="*34)
print("Student name is " + student_obj.company)