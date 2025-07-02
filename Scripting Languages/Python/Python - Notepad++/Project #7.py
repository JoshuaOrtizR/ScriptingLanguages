#Monday, October 10, 2024

#Restaurant Discount System
''''
Create a Python program that simulates a discount system in a restaurant based on the amount spent. 
The program should follow these instructions:

1. **Ask the user to enter the amount spent at the restaurant.**
2. **Apply discounts according to the following rules:**
   * If the amount spent is greater than 50 but less than or equal to 100, apply a 20% discount.
   * If the amount spent is greater than 200, apply a 30% discount.
   * If the amount spent is less than or equal to 50, no discount applies.
3. **Show the user a summary of the bill with the original amount, the discount applied, and the final amount with the discount.** 
'''
amountSpent = float(input("Please enter your Total: "))

#Discount Calculation  
if amountSpent > 50 and amountSpent <=100:
    discountPercentage = 0.1
elif amountSpent > 100 and amountSpent  <= 200:
    discountPercentage = 0.2
elif amountSpent > 200:
    discountPercentage = 0.3
else:
    discountPercentage = 0.0

#Final Amount
discount = amountSpent * discountPercentage
finalAmount = amountSpent - discount

#Output
print("\n  Total Amounts")
print(f"Monto de consumo: {amountSpent:.2f} USD")
print (f"Discount Applied: {discountPercentage * 100:.0f} %")
print(f"Fianl Amount Discounted: {finalAmount:.2f} USD")