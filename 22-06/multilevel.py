# Multilevel Inheritance
class Grandparent:
    def house(self):
        print("Grandparent owns a house")

class Parent(Grandparent):
    def car(self):
        print("Parent owns a car")

class Child(Parent):
    def bike(self):
        print("Child owns a bike")