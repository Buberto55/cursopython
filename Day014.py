from Day014_Data import data
import random

print("Jugemos aaa.... Higher Lower!!!!")

def getrandomdata(act):
    global data
    print(act)
    acum = random.choice(data)
    print(acum)
    while act == acum:
        print(acum, act, "Se repitio!")
        acum = random.choice(data)
        print(acum, act, "El nuevo")

    return acum

val1 = {}
val2 = {}

val1 = getrandomdata(val1)

print(f"compara: \n{val1}\n{val2}\ntantan")

val2 = getrandomdata(val1)

print(f"compara: \n{val1}\n{val2}\ntantan")

#game = str(input("Quieres jugar?: 'Si' o 'No': ")).lower()

