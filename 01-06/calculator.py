print("Calculator:")
print("\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
choice = int(input("Enter your choice:"))
n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))

match choice:
    case 1:
        print("Addition",n1+n2)
    case 2:
        print("Sub=",n1-n2)
    case 3:
        print("Mul=",n1*n2)
    case 4:
        print("Div=",n1/n2)
    case _:
        print("Exit")
