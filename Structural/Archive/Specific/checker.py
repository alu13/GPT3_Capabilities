
from random import shuffle

# Initialize some variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
values = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13}

# Create a deck of cards
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)

# Shuffle the deck
shuffle(deck)

# Deal the cards
player1 = []
player2 = []
for i in range(26):
    player1.append(deck.pop())
    player2.append(deck.pop())

# Helper function to print a player's cards
def printCards(player, name):
    print(name + ' has:')
    for card in player:
        print('  ' + card)

# Print each player's cards
printCards(player1, 'Player 1')
printCards(player2, 'Player 2')

# Helper function to play a single round of war
def playRound(p1, p2, name1, name2):
    # Each player plays a card
    c1 = p1.pop()
    c2 = p2.pop()

    # Compare the cards to see who wins
    v1 = values[c1.split()[0]]
    v2 = values[c2.split()[0]]
    if v1 > v2:
        # Player 1 wins the round
        print(name1 + ' wins the round with a ' + c1)
        p1.extend([c1, c2])
    elif v1 < v2:
        # Player 2 wins the round
        print(name2 + ' wins the round with a ' + c2)
        p2.extend([c1, c2])
    else:
        # It's a tie!
        print('Tie! Each player puts down three cards')

        # Put down three cards
        for i in range(3):
            p1.append(p1.pop())
            p2.append(p2.pop())

        # Play another round
        playRound(p1, p2, name1, name2)

# Play the game!
while len(player1) > 0 and len(player2) > 0:
    # Print each player's cards
    printCards(player1, 'Player 1')
    printCards(player2, 'Player 2')

    # Play a round
    playRound(player1, player2, 'Player 1', 'Player 2')

# Determine the winner
if len(player1) > 0:
    print('Player 1 wins the game!')
else:
    print('Player 2 wins the game!')