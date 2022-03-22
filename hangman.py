import random
import os
from word_lists import word_list
from hangman_art  import *
print(logo)
my_word = random.choice(word_list)
blanks=[]
lives=6
for i in my_word:
    blanks.append("-")
print("  ".join(blanks))
end_of_game = False
while not end_of_game:
    guess= input("Guess a letter\n").lower()
    if guess in blanks:
        print(f"you've already guessed {guess}")
    for position in range(len(my_word)):
        l=my_word[position]
        if l==guess:
            blanks[position]=l
    if guess not in my_word:
        print(f"you guessed {guess} that is not in the word. You lose a life!")
        lives-=1
        if lives == 0:
          end_of_game=True
          print("You Lose!")
    print("  ".join(blanks))
    if "-" not in blanks:
        end_of_game= True
        print("You Win")
    print(stages[lives])
input('press Enter to exit')


