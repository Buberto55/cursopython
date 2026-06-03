# Printing to the console

# Function print() is used to print something to the console
# The text to be printed is enclosed in quotation marks ("")
# In this case, we are printing a string of text that says "Hello World!"

print("Hello World!")

# There are different types of error that can occur when writing code. 
# One common type of error is a syntax error, which occurs when the code is not written in the correct format. 
# For example, if we forget to close the quotation marks in our print statement
# we will get a syntax error.

# Is necesary to follow the correct syntax when writing code
#--------------------------------------------------------------------------------------
# Exercise 1: Printing Practice
print("1. Mix  500g of flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Let the dough rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
#--------------------------------------------------------------------------------------
# Also we can use backslash (\) and n to create a new line in our print statement
print("Hello World!\nWelcome to Python programming.")

# We can add strings together using the + operator. This is called string concatenation.
print("Hello "+ " " + "World!")
#--------------------------------------------------------------------------------------
# Exercise 2: Fix the code below
#print(Notes from Day 1")
# print("The print statement is used to output strings")
#print("Strings are strings of characters"
#priint("String Concatenation is done with the + sign")
#print(("New lines can be created with a \ and the letter n")

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")
#--------------------------------------------------------------------------------------
# To interact with the user, we can use the input() function. 
# This function allows us to get input from the user and store it in a variable.

print("Hello "+ input("What is your name? ")+ "!")

# Python variables are used to store data.
# We can save the name  of the user in a variable and use it to print it.
user_name = input("What is your name? ")
print("Hello, " + user_name + "!")

# Also we can use the variable to update the value of the variable and print it again.
user_name = "Buberto"
print("Hello, " + user_name + "!")

# To get the length of a string, we can use the len() function.
# This function takes a string as an argument and returns the number of characters in the string.
print(len(user_name))
# So I can get the length of the name of the user directly without saving it in a variable.
print(len(input("What is your name? ")))

username = input("What is your name? ")
length = len(username)
print(length)

# Exercise 3: Variable
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1, glass2)

# Project: Band Name Generator
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in? ")
pet = input("What's your pet's name? ")
band_name = city + " " + pet
print("Your band name could be " + band_name)
