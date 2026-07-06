from tabulate import tabulate

import sqlite3

conn=sqlite3.connect("petadoption.db")

cursor = conn.cursor()

def search_by_species():
    species = input("Enter Species: ")

    query = "SELECT * FROM Pets WHERE Species = ?"

    cursor.execute(query, (species,))
    records = cursor.fetchall()

    if records:
        headers = ["Pet ID", "Name", "Species", "Breed", "Age",
                   "Gender", "Health", "Status", "Shelter ID"]
        print(tabulate(records, headers=headers, tablefmt="grid"))
    else:
        print("No pets found.")


def search_by_breed():
    breed = input("Enter Breed: ")

    query = "SELECT * FROM Pets WHERE Breed = ?"

    cursor.execute(query, ("%" + breed + "%",))
    records = cursor.fetchall()

    if records:
        headers = ["Pet ID", "Name", "Species", "Breed", "Age",
                   "Gender", "Health", "Status", "Shelter ID"]
        print(tabulate(records, headers=headers, tablefmt="grid"))
    else:
        print("No pets found.")


def search_by_age():
    age = int(input("Enter Age: "))

    query = "SELECT * FROM Pets WHERE Age = ?"

    cursor.execute(query, (age,))
    records = cursor.fetchall()

    if records:
        headers = ["Pet ID", "Name", "Species", "Breed", "Age",
                   "Gender", "Health", "Status", "Shelter ID"]
        print(tabulate(records, headers=headers, tablefmt="grid"))
    else:
        print("No pets found.")


def search_by_location():
    pass


def search_by_health_status():
    pass


def view_available_pets():
    pass


def search_menu():
    while True:
        print("\n===== SEARCH MENU =====")
        print("1. Search by Species")
        print("2. Search by Breed")
        print("3. Search by Age")
        print("4. Search by Shelter Location")
        print("5. Search by Health Status")
        print("6. View Available Pets")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            search_by_species()

        elif choice == 2:
            search_by_breed()

        elif choice == 3:
            search_by_age()

        elif choice == 4:
            search_by_location()

        elif choice == 5:
            search_by_health_status()

        elif choice == 6:
            view_available_pets()

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice")


search_menu()
