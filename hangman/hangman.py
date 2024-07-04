import random
import hangman_art
from hangman_words import word_list

chosen_word=random.choice(word_list)
length=len(chosen_word)
print(hangman_art.logo)
#print(f"Chosen word is {chosen_word}")
start=[]
for j in chosen_word:
    start.append("_")
print(f"{' '.join(start)}")
end_of_game=False
lives=6
while not end_of_game:
    guess=input("Guess a letter\n").lower()
    if guess in start:
        print(f"You've already guessed {guess}")
    for i in range(length):
        letter=chosen_word[i]
        if letter==guess:
            start[i]=letter
    print(f"{' '.join(start)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives==0:
            end_of_game=True
            print(f"YOU LOSE! The word was {chosen_word.upper()}.")
    if "_" not in start:
        end_of_game=True
        print("YOU WIN!")
    print(hangman_art.stages[lives])