# Multiple Inheritance
class Student:
    def study(self):
        print("Student studies")

class Employee:
    def work(self):
        print("Employee works")

class TeachingAssistant(Student, Employee):
    pass