#Python Calculator
operator = input("Enter an operator(+ - * /):")
num0 = float(input("First number:"))
num1 = float(input("Second number:"))

if operator == "+":
    result = num0 + num1
    print(f"Your Result is {result}")
elif operator == "-":
    result = num0 - num1
    print(f"{num0}{num1}")
elif operator =="*":
    result = num0 * num1
    print(result)
elif operator =="/":
    result = num0 / num1
    print(result)
else:
    print(f"Value Declined {operator}")

#-------------------------------------------

#python weight converter
options = input("1: Convert Pounds (LB) to Kilograms (KG) \n2: Convert Kilograms (KG) to Pounds (LB) \nSelect an option (1 or 2):")

if options == "1":
    lb = float(input("Insert your weight in Pounds (LB): "))
    convertion1 = lb * 0.453592
    print(f"{convertion1:.2f} KG")

elif options == "2":
    kg = float(input("Insert your weight in Kilograms (KG):"))
    convertion2 = kg * 2.20462
    print(f"{round(convertion2, 2)} LB")
else:
    print(f"Value has been declined:{options} Try again!")
#-------------------------------------------
#Conditional Expression
num = 5
print("Positive" if num > 0 else "Negative")
#------------------------------------------
n = 8
result = "Even" if n % 2 == 0 else "Odd"
print(result)
#------------------------------------------
num = 5
a = 6
b = 7
max_num = a if a > b else b
print(max_num)
#------------------------------------------
age = input("What is your age?: ")
age = int(age)
age = "Minor" if age <= 17 else "Adult"
print(age)
