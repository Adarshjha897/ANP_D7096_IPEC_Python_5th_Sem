# 8. Online Shopping Discount 
# Scenario: 
# An e-commerce website offers a fixed discount on products. 
# Problem Statement: 
# Write a Python program to calculate the final payable amount after applying the discount. 
# Input: 
# • Product Price  
# • Discount Amount  
# Output: 
# • Final Price 

product_price = float(input("Enter the product price: "))
discount_amount = float(input("Enter the discount amount: "))
print("Product Price: ", product_price)
print("Discount Amount: ", discount_amount)
print("Final Price: ", product_price - discount_amount)


"""
Enter the product price: 678
Enter the discount amount: 4
Product Price:   678.0
Discount Amount: 4.0
Final Price:     674.0

"""