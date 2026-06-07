# For Loop
# If we want to print all values in a list... 
frutas = ["Papa", "Pera", "Uva", "Coco"]
for fruta in frutas:
    print("Jugo de " + fruta)

#----------------------------------------------------
# Highest Score
notas = [81, 79, 84, 73, 91, 48, 75, 105, 126, 134, 105, 107, 81, 49, 171, 154, 167, 59, 123, 132, 164, 146, 159, 197, 184, 153, 199, 187, 182, 180, 70]

print(sum(notas))

notas_sum_tot = 0
for nota in notas:
    notas_sum_tot += nota

print(notas_sum_tot)

print(max(notas))

notas_max = 0
for nota in notas:
    if nota > notas_max:
        notas_max = nota

print(notas_max)
#----------------------------------------------------
# Gauss example
gauss = 0
for num in range(1,101):
    gauss += num
print(gauss)

#----------------------------------------------------
# Exercise 6: FizzBuzz
for num in range(1,101):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
#----------------------------------------------------
# Project: Password Generator
import string
import random
letras = list(string.ascii_letters)
simbolos = list(string.punctuation)
numeros = list(string.digits)
lista_t = [letras, simbolos, numeros]
print(letras)
print(numeros)
print(simbolos)

print("Generador de contraseñas!")
num_let = int(input("Cuantas letras quieres para la contraseña?: "))
num_sim = int(input("Cuantos simbolos quieres para la contraseña?: "))
num_num = int(input("Cuantos numeros quieres para la contraseña?: "))
num_total = num_let + num_sim + num_num

# Easy 
pw = ""
for val in range(0,num_let):
    pw += random.choice(letras)
print(pw)
for val in range(0,num_sim):
    pw += random.choice(simbolos)
print(pw)
for val in range(0,num_num):
    pw += random.choice(numeros)
print(pw)

# Hard
pw = ""
while num_let or num_sim or num_num:
    state = random.randint(0,2)
    if state == 0 and num_let > 0:
        pw += random.choice(letras)
        num_let -= 1
    if state == 1 and num_sim > 0:
        pw += random.choice(simbolos)
        num_sim -= 1
    if state == 2 and num_num > 0:
        pw += random.choice(numeros)
        num_num -= 1
print(pw)

# F*CK this class jajajajaja I made it by this way knoing that the function shuffle exist jajaja
# I hate it but, I did it!