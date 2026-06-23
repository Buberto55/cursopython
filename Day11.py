# Project: Blackjack

# Do we import to shuffle the deck
import random

# We set the value for keep playing, the quest to draw other card and the final move
game = True

# Define function to convert A value from 11 to 1
def aceconv(list):
    # Replace the value to 1 point
    indice = list.index(11)
    list[indice] = 1

# Define funtion to add a card
def addcard(list, q):
    # Deck:   A, 2, 3, 4, 5, 6, 7, 8, 9, 10,  J,  Q,  K.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for a in range(0, q):
        list.append(random.choice(cards))

# Define conquest function
def finalconquest(p,d):
    # Get the score between player and dealer
    scorep = sum(p)
    scored = sum(d)
    # Print the final score
    print(f"Player: {scorep} \nDealer: {scored}")
    # Compare the results to the final conquest
    if scored > 21:
        print("Ganaste!!! :D")
    elif scored > scorep:
        print("Gana el dealer! chin :c")
    elif scored < scorep:
        print("UUUUFFF Ganaste!!! :D")
    elif scored == scorep:
        print("Es un empate!!!! :o")

# This loop for keep playing
while game:

# Always empty hand for each player and reset start and finish value
    player = []
    dealer = []
# Set values of start, continue and dealer game
    start = ""
    contin = True
    delgame = True
    finish = True
    
# Ask to the player if he want to play    
    start = str(input("Comenzamos una partida? ""Si"" o ""No"": ")).lower()

    # If he say no we stop the game
    if start == "no":
        game = False
    
    # If he starts the game:
    elif start == "si":           
            # Set 2 cards for player and dealer
            addcard(player,2)
            addcard(dealer,2)
            # Consider the actual situation:
            while contin:
                # Show the cards in the game
                print(f"Jugador: {player} \n Dealer: [{dealer[0]}, #]")
                # If player already have 21 points, stop the player game
                if sum(player) == 21:
                    print("Tienes 21!!!")
                    contin = False
                # If player game is over 21 points
                elif sum(player) > 21:
                    # If he has an A in his hand:
                    if 11 in player:
                        # Convert Ace value to 1
                        aceconv(player)
                    else:
                         # Otherwise he lose
                         print("Perdiste!")
                         contin = False
                         delgame = False
                         finish = False
                # If he continue playing, ask if he want another card 
                elif contin and sum(player) < 21:
                    add = str(input("Quieres otra carta? ""Si"" o ""No"": ")).lower()
                    # If he want, give a card and continue player game
                    if add == "si":
                        addcard(player, 1)
                    # If he do not, stop player game
                    elif add == "no":
                        contin = False
            # While the dealer game is available
            while delgame:
                # Show the cards in the game
                print(f"Jugador: {player} \n Dealer: {dealer}")
                # Check if dealer has a greater value than 21
                if sum(dealer) > 21:
                    # If he have an ace
                    if 11 in dealer:
                            # Convert Ace value to 1
                            aceconv(dealer)
                # If dealer score is higher than 17
                if 17 < sum(dealer):
                    # Stop the dealer game
                    delgame = False
                else:
                    # Add a card for dealer
                    addcard(dealer, 1)
            #If the game already finish, do not show the final conquest
            if finish:
                finalconquest(p=player,d=dealer)                             
    else:
         print("No sea payaso y escriba bien...")

print("Hasta la proxima!")
