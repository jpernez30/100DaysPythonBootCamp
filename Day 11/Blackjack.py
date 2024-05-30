############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

from art import logo
import random


def genCard():
  index = random.randint(0, 12)
  return index


def sumCards(list):
  sum = 0
  for card in list:
    sum += card
  return sum



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cont = True
while (cont):

  print("Do you want to play blackjack type 'y' to play 'n' to exit")
  decision = input()

  if decision == 'n':
    cont = False
  elif decision == 'y':
    print(logo)
    genCard()
    playerCards = []
    userCards = []

    firstCard = genCard()
    secondCard = genCard()

    if cards[firstCard] == 11:
      if cards[secondCard] + cards[firstCard] > 21:
        total = 1 + cards[secondCard]
      else:
        total = cards[firstCard] + cards[secondCard]
    elif cards[secondCard] == 11:
      if cards[secondCard] + cards[firstCard] > 21:
        total = 1 + cards[firstCard]
      else:
        total = cards[firstCard] + cards[secondCard]

    playerCards.append(cards[firstCard])
    playerCards.append(genCard())

    userCards.append(genCard())
