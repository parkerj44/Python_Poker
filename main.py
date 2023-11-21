import random


def score_card(li):
  
  score = 0

  face_cards = ['K', 'J', 'Q']

  for card in li:
    if card in face_cards:
      score += 10
    elif card == 'A':
      aces += 1
    else:
      score += int(card)

  score += aces

  while score + 10 <= 21 and aces > 0:
    total += 10
    aces -= 1
  
  return score



def playgame():
  play = input("Press 'y' to start game: ")
  player_bank = 250

  while play == 'y' or play == 'Y':
    print("You are starting with ${}! Good Luck!".format(player_bank))
    pot = int(input('How much would you like to bet? '))

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

    player_score = score_card(player_hand)
    dealer_score = score_card(dealer_hand)

    print("The dealer has {}. Their score is {}".format(dealer_hand, dealer_score))
    print("You have {}. Your score is {}".format(dealer_hand, dealer_score))
    player_choice = input('Would you like to hit or stay? Press h to hit and s to stay: ')

    if player_choice == 'h' or player_choice == 'H':
      player_hand.append(cards.pop(0))
      player_score = score_card(player_hand)
      if player_score > 21:



    

playgame()
    
