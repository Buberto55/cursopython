# Control and Conditional Operators
# In this case the control is the if, elif, else function
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride the rollercoster")
else:
    print("Sorry you have to grow taller before you can ride")

# The conditional Operators are the comparison between values:
# ==, !=, >, <, >=, <=

#------------------------------------------------------------------------
# Modulo operator
# Is the remainder from a divition
# We can use it to know if a number is an odd or an even

x = int(input("Set a number: "))

if x % 2 == 0:
    print("This is an even number!", x)
else:
    print("This is an odd number!", x)
#------------------------------------------------------------------------
# Nested if statements and elif statements
# Now in the rollercoaster we need to compare the height to change the ticket price
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("How old are you? "))
    if age < 12:
        print("The ticket price is $5")
        cost = 5
    elif 12 <= age <= 18:
        print("The ticket price is $7")
        cost = 7
    else:
        print("The ticket price is $12")
        cost = 12
else:
    print("Sorry you have to grow taller before you can ride")

#------------------------------------------------------------------------
# Excercise 5: BMI Calculator with Interpretations
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
