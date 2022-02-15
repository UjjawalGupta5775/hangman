# Hangman

import random
import wordList
import art

print(art.logo)

words = wordList.word_list

chosen_word = random.choice(words)

word_length = len(chosen_word)

blanks = []
for _ in range(word_length):
    blanks += "_"
print(blanks)

lives = 6
game_over = False
while not game_over:
    guess = input("Enter your guess letter: ").lower()
    if guess in blanks:
        print(f"You have already guessed the letter {guess}")
    for position in range(0,word_length):
        if chosen_word[position] == guess:
            blanks[position] = guess
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
    
    print(art.stages[lives])
    if "_" not in blanks:
        game_over = True
        print("You won")
    print(" ".join(blanks))