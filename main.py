import random


def score_card(li):
  
  score = 0

  face_cards = ['K', 'A', 'J', 'Q']

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

    dealer_hand = []
    dealers_hidden = []
    player_hand = []

    dealers_hidden.append(cards.pop(1))
    dealer_hand.append(cards.pop(2))
    player_hand.append(cards.pop(0))
    player_hand.append(cards.pop(0))





    

playgame()
    
