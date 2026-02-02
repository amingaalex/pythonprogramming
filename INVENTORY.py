# Name: Alex Abere
# Admission Number: ADM BSCIT-05-0063/2024
# Exercise 1: Simple Inventory System

inventory = {}

while True:
    print("\n1. Add / Update Item")
    print("2. View Item")
    print("3. View Total Quantity")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        if item in inventory:
            inventory[item] += quantity
            print("Item updated successfully.")
        else:
            inventory[item] = quantity
            print("Item added successfully.")

    elif choice == "2":
        item = input("Enter item name to search: ")
        if item in inventory:
            print(f"{item}: {inventory[item]}")
        else:
            print("Item not found.")

    elif choice == "3":
        total = sum(inventory.values())
        print("Total quantity of all items:", total)

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
