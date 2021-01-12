#Step 4

import random
import hangmanWordData
import hangmanArt
import os

end_of_game = False
chosen_word = random.choice(hangmanWordData.word_list)
word_length = len(chosen_word)

lives = 6
print (hangmanArt.logo)

display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print (hangmanArt.logo)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0 :
            end_of_game = True
            print ("You lose!!")
            print (f"Correct word is {chosen_word}.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print (hangmanArt.stages[lives])