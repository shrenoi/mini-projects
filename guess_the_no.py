import random
import os
from guess_the_no_art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
continue_game = True
def easy():
  random_no = random.randint(1,100)
  print(random_no)
  for i in reversed(range(10)):
    print(f"You have {i+1} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    correct_ans = False
    if guess == random_no:
      print(f"You got it! The answer was {random_no}.")
      correct_ans = True
      break
    elif guess < random_no:
      print("Too Low.")
      if i == 0:
        break
      else:
        print("Guess Again.")
    else:
      print("Too High.")
      if i == 0:
        break
      else:
        print("Guess Again.")
    
  if not correct_ans:
    print("You've run out of guesses. You LOSE.")
    
def hard():
  random_no = random.randint(1,100)
  print(random_no)
  for i in reversed(range(5)):
    print(f"You have {i+1} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    correct_ans = False
    if guess == random_no:
      print(f"You got it! The answer was {random_no}.")
      correct_ans = True
      break
    elif guess < random_no:
      print("Too Low.")
      if i == 0:
        break
      else:
        print("Guess Again.")
    else:
      print("Too High.")
      if i == 0:
        break
      else:
        print("Guess Again.")
    
  if not correct_ans:
    print("You've run out of guesses. You LOSE.")

while continue_game:
  print(logo)
  if difficulty == 'easy':
    easy()
  else:
    hard()
  play_again = input("Do you want to play again? Type 'y' or 'n': ")
  if play_again == "n":
    continue_game = False
  else:
    os.system("cls")
    print(logo)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  