age = int(input("Enter your age:"))
if age >= 18:
    print("You are signed up")
else:
    print("You must be 18+ to sign up!")
#--------------------------------------
import math
radio = float(input("Enter the radio of the circle:"))
circunference = 2 * math.pi * radio
print(f"The Circunference is:{circunference:.2f}")

#-------------------------------------------
score=float(input("What is your score:"))
if score == 7:
    print("You have passed, Congratulations!")
elif score <= 0:
    print("Your score hasn't been uploaded yet!")
elif score >= 8:
    print("You did an outstanding job!")
else:
    print("You did noy meet the required score!")

#-----------------------------------------------
#Logical Operators
temp = 25
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor even it cancelled")
else:
    print("The outdoor event is still scheduled")
#-----------------------------------------------
