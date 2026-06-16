def greet():
    print("hello")
greet()

#fuction to find cube
def cube(num):
    print(num**3)
num=int(input("enter your number:"))
cube(5)

def getno():
    print(10)

op=getno()
print(op)

print(getno())

def add(a,b):
    return a+b
print(add(10,20))
print(add(10.5,20.3))


print("start")
try:
    print(10/0)
except ZeroDivisionError:
    print("cannot divide by zero")

print("start")
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)

try:
    a={"name":"ram"}
    print(a["name"])
    print(a["age"])
except Exception as e:
    print("key not present")
else:
    print("end")
finally:
    print("-------")


try:
    n1=int(input("enter 1st number:"))

    n2=int(input("enter 2nd number:"))


    def add():
         return n1+n2
    print(add())

    add()

except:
     print("enter numbers only!!!")


class demo:
     c_name="xyz"

     def __init__(self):
        print("default constructor called")

print(demo.c_name)

obj=demo()
print(obj.c_name)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=student("ram",20)
print(s1.name)
s2=student("sita",19)
print(s2.name)

class student:
    c_name="xyz"

    #class method
    @classmethod
    def change_c_name(cls):
        return "class method"
    
    @classmethod
    def change_c_name1(cls,new_value):
        cls.c_name=new_value;
        return f"updated value is {cls.c_name}"
    
print(student.change_c_name())
print(student.change_c_name1("linkcode"))
       





