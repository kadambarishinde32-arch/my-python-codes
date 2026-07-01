from single import Dog
from multiple import TeachingAssistant
from multilevel import Child
from hierarchical import Car, Bike
from hybrid import TeachingAssistant1

print("1. Single Inheritance")
print("2. Multiple Inheritance")
print("3. Multilevel Inheritance")
print("4. Hierarchical Inheritance")
print("5. Hybrid Inheritance")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        d = Dog()
        d.eat()
        d.bark()

    case 2:
        ta = TeachingAssistant()
        ta.study()
        ta.work()

    case 3:
        c = Child()
        c.house()
        c.car()
        c.bike()

    case 4:
        c = Car()
        b = Bike()
        print("Car:")
        c.start()
        print("Bike:")
        b.start()

    case 5:
        ta = TeachingAssistant1()
        ta.speak()
        print("Teaching Assistant is both a Student and an Employee")

    case _:
        print("Invalid choice")