print("----Calculator----")
print("\n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Exit")

ch=int(input("Enter your Choice:"))

match ch:
    case 1:
        n1=int(input("Enter 1st no. :"))
        n2=int(input("Enter 2nd no. :"))
        print("Addition:",n1+n2)
        
    case 2:
        n1=int(input("Enter 1st no. :"))
        n2=int(input("Enter 2nd no. :"))
        print("Substraction:",n1-n2)
    
    case 3:
        n1=int(input("Enter 1st no. :"))
        n2=int(input("Enter 2nd no. :"))
        print("Multiplication:",n1+n2)
    
    case 4:
        n1=int(input("Enter 1st no. :"))
        n2=int(input("Enter 2nd no. :"))
        print("Divison:",n1+n2)
    
    case _:
        print("Exit")
