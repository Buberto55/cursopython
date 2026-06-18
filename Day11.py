# Project: Blackjack

# Do we import to shuffle the deck
import random

# Deck:   A, 2, 3, 4, 5, 6, 7, 8, 9, 10,  J,  Q,  K.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# We set the value for keep playing, the quest to draw other card and the final move
game = True


# This loop for keep playing
while game:

# Always empty hand for each player and reset start and finish value
    player = []
    dealer = []

    start = ""
    contin = True
    delgame = True

# We ask to the player if he want to play    
    start = str(input("Comenzamos una partida? ""Si"" o ""No"": ")).lower()

    # If he say no we stop the game
    if start == "no":
        game = False
    
    # If he starts the game:
    if start == "si":           
            # Set 2 cards to the player and one to the dealer
            player = [random.choice(cards), random.choice(cards)]
            dealer.append(random.choice(cards))
            # Consider the actual situation:
            while contin:
                # Show the cards in the game
                print(f"Jugador: {player} \n Dealer: {dealer}")
                # If player game is over 21 points
                if sum(player) > 21:
                    # If he has an A in his hand:
                    if 11 in player:
                        # Replace the value to 1 point
                        indice = player.index(11)
                        player[indice] = 1  
                    else:
                         # Otherwise he lose
                         print("Perdiste!")
                         contin = False
                         delgame = False
                elif contin and sum(player) < 21:
                    add = str(input("Quieres otra carta? ""Si"" o ""No"": ")).lower()
                    if add == "si":
                        player.append(random.choice(cards))
                    elif add == "no":
                        contin = False
                elif sum(player) == 21:
                    print("Tienes 21!!!")
                    contin = False
            while delgame:
                dealer.append(random.choice(cards))
                # Show the cards in the game
                print(f"Jugador: {player} \n Dealer: {dealer}")
                if 17 < sum(dealer):
                    delgame = False
            scoreplayer = sum(player)
            scoredealer = sum(dealer)
            print(scoreplayer, scoredealer)
            if scoredealer > 21:
                print("Ganaste!!! :D")
            elif scoredealer > scoreplayer:
                print("Gana el dealer! chin :c")
            elif scoredealer == scoreplayer:
                print("Es un empate!!!! :o")
                                  
    else:
         print("No sea payaso y escriba bien...")

print("Hasta la proxima!")
