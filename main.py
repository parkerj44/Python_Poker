import random


def score_card(li):
  ''' score_card takes the hand that is dealt in blackjack then counts it.
      It takes into account face cards and utilizes Aces in the best way to get close to 21
  '''

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

  #Loop to check if aces should be 1 or 11
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
    player_bank -= pot

    #shuffle a deck of 52 cards
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = cards * 4
    random.shuffle(cards)

    dealer_hand = []
    dealers_hidden = []
    player_hand = []

    #gives dealer and user cards from top of deck
    #dealers_hidden is so that it is not shown in score
    dealers_hidden.append(cards.pop(1))
    dealer_hand.append(cards.pop(2))
    player_hand.append(cards.pop(0))
    player_hand.append(cards.pop(0))

    player_score = score_card(player_hand)
    dealer_score = score_card(dealer_hand)

    print("The dealer has {}. Their score is {}".format(dealer_hand, dealer_score))
    print("You have {}. Your score is {}".format(dealer_hand, dealer_score))

    if player_score == 21:
      dealer_hand.append(dealers_hidden)
      dealers_score = score_card(dealer_hand)
      if dealer_score == 21:
        print('You and the dealer have 21! You will will receive back your original bet.')
        player_bank += pot
      else:
        player_bank += (pot * 2)
        print('You got BlackJack! You won ${}. You now have ${}.'.format(pot * 2, player_bank))
    else:
      player_choice = input('Would you like to hit or stay? Press h to hit and s to stay: ')

      if player_choice == 'h' or player_choice == 'H':
        player_hand.append(cards.pop(0))
        player_score = score_card(player_hand)
        if player_score > 21:
          player_bank -= pot
          print('You are over 21. You lost!')
        



    

playgame()
    
