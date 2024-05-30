import random
import os
from blackjackart import logo
def card_gen():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cardlist):
  if sum(cardlist) == 21 and len(cardlist) == 2:
    return 0
  
  if 11 in cardlist and sum(cardlist)>21:
    cardlist.remove(11)
    cardlist.append(1)
  return sum(cardlist)

def check_winner(myscore,compscore):
  if myscore > 21 and compscore > 21:
    return "YOU LOSE, YOU WENT OVER."
  
  if myscore == compscore:
    return "DRAW"
  elif compscore == 0:
    return "YOU LOSE, COMPUTER HAS BLACKJACK"
  elif myscore == 0:
    return "YOU WIN"
  elif myscore > 21:
    return "YOU LOSE, YOU WENT OVER"
  elif compscore > 21:
    return "YOU WIN, COMPUTER WENT OVER"
  elif myscore > compscore:
    return "YOU WIN"
  else:
    return "YOU LOSE"
  
def play():
  print(logo)
  mycards = []
  compcards = []
  is_game_over = False
  for i in range(2):
    mycards.append(card_gen())
    compcards.append(card_gen())

  while not is_game_over: 
    myscore = calculate_score(mycards)
    compscore = calculate_score(compcards)
    print(f"Your cards: {mycards}, current score: {myscore}")
    print(f"Computer's first card: {compcards[0]}")
    if myscore == 0 or compscore == 0 or myscore > 21:
      is_game_over = True
    else:
      more_card=input("Type 'y' to get another card, type 'n' to pass: ")
      if more_card == "y":
        mycards.append(card_gen())
      else:
        is_game_over = True
  while compscore != 0 and compscore < 17:
    compcards.append(card_gen())
    compscore=calculate_score(compcards)
  print(f"Your cards: {mycards}, final score: {myscore}")
  print(f"Computer cards: {compcards}, final score: {compscore}")
  print(check_winner(myscore,compscore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("cls")
  play()