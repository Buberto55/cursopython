# Hangedman game
import random

lista_palabras = ["perro", "gato", "marciano"]

pal_sec = random.choice(lista_palabras)
esp_bla = ""
# Part 1 ---------------------------------------------
#print(pal_sec)
#state = 2
#letra = str(input("Adivina una letra: ")).lower()
#for a in pal_sec:
#    if a == letra:
#        print("Si")
#    else:
#        print("No")

# Part 2 ---------------------------------------------
#print(pal_sec)
#for a in pal_sec:
#    esp_bla += "_"
#print(esp_bla)

#adiv = list(esp_bla)
#count = 0
#letra = str(input("Adivina una letra: ")).lower()
#for a in pal_sec:
#    if a == letra:
#        adiv[count] = letra
#    count += 1
#count = 0
#print("".join(adiv))

# Part 3 ---------------------------------------------
print(pal_sec)
for a in pal_sec:
    esp_bla += "_"
print(esp_bla)

adiv = list(esp_bla)
count = 0
state = True
vidas = 6
while state == True:
    letra = str(input("Adivina una letra: ")).lower()

    if letra in pal_sec:
        for a in range(len(pal_sec)):
            if pal_sec[a] == letra and adiv[a] == "_":
                adiv[a] = letra
        print("".join(adiv))
        if not "_" in adiv:
            print("Ganaste!!")
            state = False

    elif not letra in pal_sec and vidas > 0:
        print("ups, vida menos")
        vidas -= 1
        print("vidas:",vidas)
        if vidas == 0:
            print("Perdiste :c")
            state = False
# I finished with all de conditions before part 4 and 5, so I concluded the code with my own knowledge!!!