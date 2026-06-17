# Project: Blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while game:

    player = []
    dealer = []

    game = True
    start = ""
    finish = False
    
    start = str(input("Comenzamos una partida? ""Si"" o ""No"": ")).lower()
    
    if start == "no":
        game = False
    
    elif start == "si":           
            player = [random.choice(cards), random.choice(cards)]
            dealer.append(random.choice(cards))
            print(f"Jugador: {player} \n Dealer: {dealer}")
            
            while sum.player < 21 or finish:
                if sum.player > 21:
                    if 11 in player:
                        indice = player.index(11)
                        player[indice] = 1                
                else:
                     
                     print("Perdiste! lerolero")
            
                add = str(input("Quieres otra carta? ""Si"" o ""No"": "))

                if add == "si":
                     player.append(random.choice(cards))
            
    else:
         print("No sea payaso y escriba bien...")

print("Hasta la proxima!")