# More functions but inputs!
def greet():
    print("Hola")
    print("Papucho")
    print("Hermoso")

greet()

def greet_w_name(name): # Here "name" is a parameter
    print(f"Hola {name}")
    print(f"Si te bañaste {name}?")
    print(f"Hueles a pedo {name}!")

greet_w_name("Nacho") # Here "Nacho" is an argument

# Exercise 7: Life in weeks
def life_in_weeks(old, age):
    left = (old - age) * 52
    print(f"You have {left} weeks left")

life_in_weeks(80,30)

def nodigasmmds(ca, qui, ta):
    print(f"Ni te sabes la de: {ca}")
    print(f"Chupa limon con: {qui}")
    print(f"No se como se me quita: {ta}")

nodigasmmds(ta="ni modo", ca="callarte un rato", qui="cabezon sin calzon")

# Exercise 8: Love calculator
import string
def calculate_love_score(name1, name2):
    true = 0
    love = 0
    first = ["t","r","u","e"]
    secound = ["l","o","v","e"]
    names = name1.lower() + name2.lower()
    for letter in names:
        if letter in first:
            true += 1
        if letter in secound:
            love += 1
    print(str(true)+str(love))

calculate_love_score("Tru", "Lov")

# Project: Caesar Cipher
abcd = list(string.ascii_lowercase)
encry = []
jumps = []
mesaje = []

def encryp(msng, shift):
    for letter in msng:
        jumps.append(abcd.index(letter))
        if abcd.index(letter) + shift > 25:
            encry.append(abcd.index(letter) + shift - 26)
        else:
            encry.append(abcd.index(letter) + shift)
#print(jumps)
#print(encry)
    for letter in range(0,len(msng)):
        mesaje.append(abcd[encry[letter]])
    print("".join(mesaje))


encryp(msng=input("Escribe el mensaje: ").lower(), shift=int(input("Escribe el desfase del mensaje: ")))
#print(len(abcd))
#print(abcd)
#msng = input("Escribe el mensaje: ").lower()
#shift = int(input("Escribe el desfase del mensaje: "))




