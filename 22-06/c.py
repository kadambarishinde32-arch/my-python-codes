from p1 import one
from p2 import two
class c(one,two):
        def pqr(self):
            print("im from child pqr")

        def call_p2_show(self):
              return two.show(self)
        
        def __init__(self, name,age):
              print("c con")
              one.__init__(self,name)
              two.__init__(self,age)
        
#object
obj=c("ram",20)
# obj.xyz()
# obj.abc()
# obj.pqr()
# obj.show()
# obj.call_p2_show()

        