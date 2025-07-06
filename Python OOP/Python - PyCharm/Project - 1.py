#01/07/2025
#Strings
file = "Compromised"
print(f"This file has been {file}")

#integers
age = 26
print(f"I am {age} years old")

#Float
final_price = 14.99
print(f"The final price is {final_price} USD")

#Boolean (Yes/No)
student = False
if student:
    print(f"You are a Programmer")
else:
    print(f"You are not a Programmer")

#Typecasting
n = "Joshua"
a = 26
height = 1.71
is_programmer = True

height = int(height)
print(height)

a = float(a)
print(a)

a = str(a)
print(a)
print(type(a))

#-----------------------------------------------------------------------------------
#Temperature Converter

#unit = input("Is this temperature in Celcius or Fahrenheit: (C/F)")
options = input(" Fahrenheit to Celsius (1) \n Celsius to Fahrenheit (2) \n Select (1 or 2):")
temp = float(input("Enter the temperature:"))

if options == "1":
    score1 = round((temp * 9) / 5 + 32, 2)
    print(f"Fahrenheit Temperature: {score1:.2f} °F")
elif options == "2":
    score2 = round((temp - 32) * 5 / 9, 2)
    print(f"Celcius Temperature: {score2:.2f} °C")
else:
    print(f"No valid measure: {options}")





