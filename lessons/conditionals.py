"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("i am thinking of a number between 1-5, what is it?")
guess: int = int(input("what is your guess? "))

if guess == SECRET:
    print("you guessed right!")
else:
    print("sorry ur wrong")
     
print("Game over.")