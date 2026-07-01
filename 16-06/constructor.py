globalvar="hey"
class demo:
    pass
    msg="hello"
    def __init__(self):
        print("created!")

    def __init__(self,age):
        self.name="xyz"
        self.age=age

    def __del__(self):
        print("deletef")

    def access_globalvar(self):
        print(globalvar)
        local_var=90
        print("local_war")

obj=demo(20)
         