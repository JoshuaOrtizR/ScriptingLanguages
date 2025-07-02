#Saturday, October 05, 2024
number = int(input("Enter a number: ")) 

if number > 0:
    if number % 2 == 0:
        print(f"The number {number} is even(+). ")
    else:
        print(f"The number {number} is not even(+). ")
elif number < 0:
    if number % 2 == 0:
        print(f"The number {number} is even (-). ")
    else:
        print(f"The number {number} is not even. ")