import random
import stages
import words

chosen_word = random.choice(words.word_list)

print(stages.logo)

display = []

for letter in chosen_word:
    display += "_"


lives = 6
end_of_game = False
print(stages.stage[6])
print(display)
while not end_of_game:

    guess = input("Guess the letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(stages.stage[lives])
        print(f"You have {lives} left")
    if lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The word was {chosen_word}")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!")
