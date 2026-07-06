"""

Lab 4: Inventory Management 
Problem Statement: 
Create a dictionary to maintain the stock of products in a shop. 
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
Implement the following: 
• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
• Display products having stock less than 20.  
• Display the total number of items available in the inventory. 


"""
# Lab 4: Inventory Management

# Initial inventory dictionary
inventory = {
    'Laptop': 15,
    'Mouse': 40,
    'Keyboard': 25,
    'Monitor': 10
}

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add a new product")
    print("2. Update stock of an existing product")
    print("3. Remove a product from inventory")
    print("4. Display products with stock less than 20")
    print("5. Display total number of items in inventory")
    print("6. Display all products")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    # 1. Add a new product
    if choice == "1":
        product = input("Enter product name: ")
        stock = int(input("Enter stock quantity: "))
        inventory[product] = stock
        print(f"{product} added successfully!")

    # 2. Update stock of an existing product
    elif choice == "2":
        product = input("Enter product name to update: ")
        if product in inventory:
            stock = int(input("Enter new stock quantity: "))
            inventory[product] = stock
            print(f"Stock of {product} updated successfully!")
        else:
            print("Product not found in inventory.")

    # 3. Remove a product from inventory
    elif choice == "3":
        product = input("Enter product name to remove: ")
        if product in inventory:
            del inventory[product]
            print(f"{product} removed successfully!")
        else:
            print("Product not found in inventory.")

    # 4. Display products with stock less than 20
    elif choice == "4":
        print("\n--- Products with Stock Less Than 20 ---")
        found = False
        for product, stock in inventory.items():
            if stock < 20:
                print(f"{product}: {stock}")
                found = True
        if not found:
            print("No products with stock less than 20.")

    # 5. Display total number of items in inventory
    elif choice == "5":
        total_items = sum(inventory.values())  # sum of all stock values
        print(f"\nTotal number of items in inventory: {total_items}")

    # 6. Display all products
    elif choice == "6":
        print("\n--- Current Inventory ---")
        for product, stock in inventory.items():
            print(f"{product}: {stock}")

    # 7. Exit
    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
