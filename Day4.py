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
player = int(input("Hora de jugar! Selecciona: \n1 ► Piedra\n2 ► Papel\n3 ► Tijera\n Jugador: "))
cpu = random.randint(1,3)
jugada = {1:"Piedra", 2:"Papel", 3:"Tijera"}

if player < 1 or player > 3:
    print("que del 1 al 3 saaaaaaaaaaaaaaaabe")
else:
    print(f"Jugador: {jugada[player]} VS CPU: {jugada[cpu]}")
    if (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
        print("Ganaste!")
    elif player == cpu:
        print("Empate")
    else:
        print("Perdiste :c")

# Now there is an easyer way to solve this problem:
resultado = (player - cpu) % 3

if resultado == 0:
    print("Empate")
elif resultado == 1:
    print("Ganaste")
else:
    print("Perdiste")

# This is because we are considering the properties of the values of rock, paper, scissors as 1, 2, 3
# And is more complicated just because how python solve the module ecuation that give the module results

