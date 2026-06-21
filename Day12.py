# Local and Global variables

#This is an example of a variable in the hole code that can be accesible
enemigos = 1

# Otherwise the variable inside this function only works here
def increnemigos (enem):
    # How do we take a global value??? Use global connotation!!!
    # global enemigos
    # enemigos += 1
    # print(f"Valor de enemigos dentro de la funcion: {enemigos}")
    return enem + 1

# Execute the function to show the local value 
enemigos = increnemigos(enemigos)
# Print the golbal value that is outside the function
print(f"Valor de enemigos fuera de la funcion: {enemigos}")

# There is no block scope in python!!!

# Global constant are declared by capitals!!!!!
# Python do not tells you, is just a way to do not forget that

# PI = 3.14159
# GOOGLE_URÑ = www.google.com

# Exercise 11: Prime number checker
# Works checking all divition posible between 2 and half of the number
def is_prime(num):
    half = num // 2
    for number in range(2, half + 1):
        if num % number == 0:
            return False
    return True

# Project: The number guessing name

from random import randint

def numguess(dif,tst):
    
    intent = 0
    numsec = 0
    
    if dif == "facil":
        intent = 10
    elif dif == "dificil":
        intent = 5
    else:
        return print("Error en la opcion, escriba bien perro")
    
    numsec = randint(1,100)

    if tst:
        print(f"E we... no le digas a nadie pero el numero secreto es: {numsec}")
    
    print(f"Tienes {intent} intentos...")

    while intent:
        
        intent -= 1
        
        intnum = int(input("Escribe un numero: "))

        if intnum > numsec and intent != 0:
            print("Menos...")
        elif intnum < numsec and intent != 0:
            print("Mas...")
        elif intnum == numsec:
            return print("Ganaste!!! :D")
       

        if intent > 0:
            print(f"Quedan: {intent}")
    
    return print("Perdiste... :c")


print("Adivina el numero!\nEstoy pensando en un numero entre el 1 y 100!")

dificultad = str(input("'Facil' o 'Dificil': ").lower())
numguess(dificultad, 0)

# After this project am going to build every project learning how IA develops and how it uses the basic and advanced concepts in Python