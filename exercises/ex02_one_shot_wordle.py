"""EX02 - One-shot Wordle."""
__author__ = "730566062"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")

i: int = 0
emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if guess != secret_word:
    print("Not quite. Play again soon!")
if guess == secret_word:
    print("Woo! You got it!")

while len(guess) > len(secret_word):
    guess = input("That was not 6 letters! Try again: ")
while len(guess) < len(secret_word):
    guess = input("That was not 6 letters! Try again: ")

while i < 6:
    if secret_word[i] == guess[i]:
        emoji = emoji + GREEN_BOX  
    else:
        incorrect_letter: bool = False
        index: int = 0
        while not incorrect_letter and index < len(secret_word):
            if secret_word[index] == guess[i]:
                incorrect_letter = True
            index = index + 1
        if incorrect_letter is True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    i = i + 1
print(emoji)
