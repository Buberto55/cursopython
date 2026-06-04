# len function only counts the number of characters in a string, including spaces and punctuation.
#print(len(123456))
# The above code will give an error because the len() function can only be used with strings, lists, tuples, and other iterable objects.

# Subscripting
print("Subscripting")
# Is a way to access individual characters in a string.
print("Hello World!"[0])
print("Hello World!"[6])
print("Hello World!"[-1])
print("Hello World!"[-7])
print("\n")

# String
print("String")
print("Ho"+"la") #Concatenation
print("Ho"*3) #Repetition
print("\n")

# Integers
print("Integers")
print(2+3, type(2+3)) #Addition
print(2-3, type(2-3)) #Subtraction
print(2*3, type(2*3)) #Multiplication
print(2/3, type(2/3)) #Division
print(2//3, type(2//3)) #Floor Division
print(2%3, type(2%3)) #Modulus
print(2**3, type(2**3)) #Exponentiation
print("\n")

# Floats
print("Floats")
print(2.5+3.5, type(2.5+3.5)) #Addition
print(2.5-3.5, type(2.5-3.5)) #Subtraction
print(2.5*3.5, type(2.5*3.5)) #Multiplication
print("\n")

# Booleans
print("Booleans")
print(True and False, type(True and False)) #Logical AND
print(True or False, type(True or False)) #Logical OR
print(not True, type(not True)) #Logical NOT
print("\n")

# type() function is used to check the type of a variable.
print("Type Checking")
print(type("Hello World!")) #String
print(type(2)) #Integer
print(type(2.5)) #Float
print(type(True)) #Boolean
print("\n")

# Also we can use int(), float(), str() and bool() functions 
# to convert between different types.
print("Type Conversion")
print(int("23574"), type(int("23574"))) #Converts string to integer
print(float("2.5"), type(float("2.5"))) #Converts string to float
print(str(255), type(str(255))) #Converts integer to string
print(bool(int("0")), type(bool(int("0")))) #Converts string to boolean 
# (0 is False, any other number is True)
print("\n")


# We print the length of the name of the user directly without saving it in a variable.
print("Tu nombre tiene " + str(len(input("¿Cuál es tu nombre? "))) + " caracteres.")

# Other way to do it is to save the name of the user in a variable and then print the length of the name.
username = input("¿Cuál es tu nombre? ")
length = len(username)
print("Tu nombre tiene " + str(length) + " caracteres.")

print(3*3/3+3-3)

# Exercise 4: BMI Calculator
height = 1.65
weight = 84
bmi = weight / height**2
print(bmi)

# We can also round the BMI to 2 decimal places using the round() function.
bmi = round(weight / height**2, 2)
print(bmi)

print(round(bmi, 2))

# Incrementing and Decrementing
# We can use the += and -= operators to increment and decrement a variable.
score = 0
score += 1 # Incrementing
print(score)
score -= 1 # Decrementing
print(score)

# Using f-strings to print the score
score += 1
if score > 0:
    is_winning = True
else:
    is_winning = False
    
print(f"Your score is {score}. You are winning: {is_winning}")

# Project: Tip Calculator
print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

