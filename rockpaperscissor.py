import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice=int(input())
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
compchoice=random.randint(0,2)
game=[rock,paper,scissors]
if choice>=3 or choice<0:
  print("Invalid input. You Lose!")
else:
  print(game[choice])
  print("Computer chose: ")
  print(game[compchoice])
  if choice==0 and compchoice==2:
    print("You Win!")
  elif compchoice==0 and choice==2:
    print("You Lose!")
  elif compchoice>choice:
    print("You Lose!")
  elif choice>compchoice:
    print("You Win!")
  else:
    print("It is a DRAW")


