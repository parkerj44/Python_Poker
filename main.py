import random


def deal_cards(li):
  
  hand = []

  while len(hand) < 2:
    hand.append(li.pop(random.randrange(len(li))))
  
  return hand



def playgame():
  play = input("Press 'y' to start game: ")

  while play == 'y':
    player_bank = 250
    print("You are starting with $250! Good Luck!")

    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = cards * 4
    random.shuffle(cards)

    dealer_hand = deal_cards(cards)

    print(dealer_hand)
    print(cards)
    break

    

playgame()
    
