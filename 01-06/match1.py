ch= int(input("Enter a Choice:"))

match ch:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend")
    case _:
        print("Invalid Choice")
