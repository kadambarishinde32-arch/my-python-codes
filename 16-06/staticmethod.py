
class demo:
    pass
    msg="hello"
@classmethod
def display_classvar(cls):
    return "hi"

def __init__(self,age):
    self.name="xyz"
    self.age=age

def display(self):
    print(f"name is {self.name} & age is {self.age}")

def greet(name,objref):
    return f"hello gm {name}{demo.msg}{objref.age}!"

obj=demo()
print(obj.display_classvar())





