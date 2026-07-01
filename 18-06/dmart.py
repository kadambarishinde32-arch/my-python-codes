class Dmart:
    storename = "DMART"

    def __init__(self, category, p_name, qty, price):
        self.category = category
        self.p_name = p_name
        self.qty = qty
        self.price = price

    @classmethod
    def display_store(cls):
        return f"Store Name : {cls.storename}"

    def common_features(self):
        return (f"Category : {self.category}\n"
                f"Product Name : {self.p_name}\n"
                f"Available Quantity : {self.qty}\n"
                f"Price : {self.price}")


class Clothes(Dmart):
    def __init__(self, category, p_name, qty, price, colour, size):
        super().__init__(category, p_name, qty, price)
        self.colour = colour
        self.size = size

    def display_clothes(self):
        print(self.display_store())
        print(self.common_features())
        print("Colour :", self.colour)
        print("Size :", self.size)


class Grocery(Dmart):
    def __init__(self, category, p_name, qty, price, brand, mfg, exp):
        super().__init__(category, p_name, qty, price)
        self.brand = brand
        self.mfg = mfg
        self.exp = exp

    def display_grocery(self):
        print(self.display_store())
        print(self.common_features())
        print("Brand :", self.brand)
        print("MFG :", self.mfg)
        print("EXP :", self.exp)


# Objects
cloth = Clothes("Clothes", "Jeans", 100, 799, "Blue", "M")
grocery = Grocery("Grocery", "Sugar", 60, 100, "SugarLite",
                  "2026-06-01", "2027-06-01")

orders = []

while True:

    print("\n------WELCOME TO DMART------")
    print("1. Grocery Section")
    print("2. Clothing Section")
    print("3. Purchase")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    match choice:

        case 1:
            grocery.display_grocery()

        case 2:
            cloth.display_clothes()

        case 3:

            while True:

                print("\n1. Buy Grocery")
                print("2. Buy Clothes")
                print("3. Generate Bill")
                print("4. Back to Main Menu")

                ch = int(input("Enter choice : "))

                if ch == 1:
                    qty = int(input("Enter quantity : "))

                    total = qty * grocery.price

                    orders.append([grocery.p_name,
                                   qty,
                                   grocery.price,
                                   total])

                    print("Item Added Successfully!")

                elif ch == 2:
                    qty = int(input("Enter quantity : "))

                    total = qty * cloth.price

                    orders.append([cloth.p_name,
                                   qty,
                                   cloth.price,
                                   total])

                    print("Item Added Successfully!")

                elif ch == 3:

                    if len(orders) == 0:
                        print("No items purchased!")

                    else:
                        grand_total = 0

                        print("\n-----------BILL-----------")
                        print("Product\tQty\tPrice\tTotal")

                        for item in orders:
                            print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
                            grand_total += item[3]

                        print("--------------------------")
                        print("Grand Total =", grand_total)

                    break

                elif ch == 4:
                    break

                else:
                    print("Invalid Choice!")

        case 4:
            print("Thank You!!!")
            break

        case _:
            print("Invalid Choice!")