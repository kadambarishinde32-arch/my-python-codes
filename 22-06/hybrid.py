# Hybrid Inheritance
class Person:
    def speak(self):
        print("Person can speak")

class Student1(Person):
    pass

class Employee1(Person):
    pass

class TeachingAssistant1(Student1, Employee1):
    pass