class payment:
    def pay(self):
        pass
    print("payment process started...")

class upi(payment):
    def pay(self):
        return "payment done by upi"
    
class gpay(payment):
    def pay(self):
        return "payment done by gpay"
    
class payment_module:
    def payment_process(self,obj):
        print(obj.pay())

p=payment_module()
u=upi()
g=gpay()

print("payment")
print("1.upi \n 2.gpay \n 3.card \n 4.exit")
choice = int(input("enter your choice\n"))
match choice:
    case 1:
        obj=upi()
        print(u.pay())
    case 2:
        obj=gpay()
        print(g.pay())
    case 3:
        pass
    case 4:
        exit()
    case _ :
        print("invalid choice!!")


p.payment_process(obj)

#multiple obj
obj=[upi(),gpay()]
for i in obj:
    print(i.pay())