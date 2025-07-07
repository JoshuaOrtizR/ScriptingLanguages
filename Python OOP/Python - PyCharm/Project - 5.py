# Nested Ternary Operator
gender = input("Insert M for (Masculine) or F (Femenine): ")
gender = "Masculine" if gender.upper() == "M" else "Femenine" if gender.upper() == "F" else "Not valig Argument"
print(gender)

#Temperature Status
temp = input("Enter temperature in Celsius: ")
temp = float(temp)
temp = "Freezing" if temp <= -5 else "Cold" if temp <= 10 else "Warm" if temp >= 11 else "No valid Number"
print(temp)

# Grade Calculator
grade = input("Enter The Numeric Score (1-100): " )
grade = float(grade)
grade = "A" if grade >= 90 else \
       ("B" if grade >= 80 else \
         ("C" if grade >=70 else "F"))
print(grade)