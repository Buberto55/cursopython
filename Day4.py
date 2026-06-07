# Randome Module
# This module helps to generate a random number between a range of numbers
# To use it is necesary to import the random library
import random

#random_integer = random.randint(1,10)
#print(random_integer)

#random_0_1 = random.random()
#print(random_0_1)

#random_float = random.uniform(1,10)
#print(random_float)

random_AoS = random.randint(0,1)
if random_AoS == 0:
    print("Sello")
else:
    print("Aguilas")

#------------------------------------------------------------

# List
# Is literaly a list of values ordered
# The order is:   0        1        2        3         4          5
list_fruits = ["Apple", "Pear", "Orange", "Peach", "Grape", "Watermelon"]
# Also can be:   -6       -5       -4       -3        -2         -1
print(list_fruits[0])

# We can edit a value directly 
list_fruits[0] = "Pineapple"
print(list_fruits[0])

list_fruits.extend(["esto no", "puede ser"])

for fruta in list_fruits:
    print(fruta)

#------------------------------------------------------------
# Let's print a random name who will pay the bill
friends = ["Pablo", "Miguel", "Juan", "Lilia", "Carlos"]
print(random.choice(friends))
# Using random.randint
print(friends[random.randint(0,4)])

# Let's practice the request from a nested list
salon_1 = ["Meche", "Vero", "Claudia", "Hector", "Paula"]
salon_2 = ["Julian", "Manuel", "Pedro", "Luis", "Tio"]

salones = [salon_1, salon_2]
print(salones)
print(salones[1][1])

# Project: Rock, Papper, Scissors
opc = input(int("Hora de jugar! Selecciona: \n1 ► Piedra\n2 ► Papel\n3 ► Tijeras"))
