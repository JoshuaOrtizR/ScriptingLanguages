#input
name = input("Who are you?:")
print("A pleasure meeting you")
age =int(input("How old are you?:"))
print(f"Nice to meet you {name}!")
age = age +1
print(f"You are {age} years old")

#-----------------------------------
length = input("Insert Length:")
width = input("Insert width:")
print("Processing Request...")

area = float(length) * float(width)

print(f"The final Area is {area}")

#--------------------------------------
tem = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many?:"))
total = price * quantity
print(f"You've bought {quantity} {item}/s at: {price} USD")

print(f"Final Total: {total:.2f} USD")
print("\nThank you for your purchase!")

#----------------------------------------------------
import math

radio = float(input("Enter the radio of the circle:"))
circunference = 2 * math.pi * radio
print(f"The Circunference is:{circunference:.2f}")