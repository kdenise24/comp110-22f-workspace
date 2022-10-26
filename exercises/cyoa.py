"""EX06 - Choose Your Own Adventure."""
__author__ = "730566062"

from random import randint

player: str = ""
points: int = 1
global easy
global hard
global guess
guess: int
easy_var: int = randint(1, 20)
hard_var: int = randint(1, 20)

EXCLAMATION: str = "\U0000203C"
STAR_EYES: str = "\U0001F929"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    global guess
    greet()
    game_selection: str = input("Would you like EASY or HARD? ... OR would you like to QUIT? ")
    if game_selection == "EASY":
        print(f"Perfect Choice {player}! Let's begin.")
        easy()
        correct_guess_easy(guess)
    if game_selection == "HARD":
        print(f"Perfect Choice {player}! Let's begin.")
        hard()
        correct_guess_hard(guess)
    if game_selection == "QUIT":
        print("Come back soon!")
        quit()


def greet() -> None:
    """Greets the player, and assigns the name."""
    global player
    player = input("What is your name? ")
    print(f"Hello {player}! I am the NUMBER GUESSING GAME{EXCLAMATION}")


def easy() -> int:
    """Recieves the guess, and asks for the input."""
    global guess
    global easy
    print(" ")
    print(f"=== Turn {str(points)}/20 ===")
    guess = int(input("Guess a number between 1-20: "))
    return guess


def hard() -> int:
    """Recieves the guess, and asks for the input."""
    global hard
    global guess
    print(" ")
    print(f"=== Turn {str(points)}/20 ===")
    guess = int(input("Guess a number between 1-100: "))
    return guess


def correct_guess_easy(guess_int: int) -> None:
    """Checks if the guess is correct and responses accordingly, also keeps track of how many turns the player has taken."""
    global points
    global player
    global easy_var
    global guess
    if guess == easy_var:
        print("You won in " + str(points) + "/20 turns!")
        print(f"CONGRATS, you know have bragging rights {STAR_EYES}.")
        print(quit())
    else:
        if points < 20:
            print("Try Again.")
            points += 1
            return correct_guess_easy(easy())
        else:
            print(" ")
            print("=== Turn X/20 ===")
            print("YOU HAVE LOST. Try again later!")
    

def correct_guess_hard(guess_int: int) -> None:
    """Checks if the guess is correct and responses accordingly, also keeps track of how many turns the player has taken."""
    global points
    global player
    global hard_var
    global guess
    if guess == hard_var:
        print("You won in " + str(points) + "/20 turns!")
        print(f"CONGRATS, you know have bragging rights {STAR_EYES}.")
        print(quit())
    else:
        if points < 20:
            print("Try Again.")
            points += 1
            return correct_guess_hard(hard())
        else:
            print(" ")
            print("=== Turn X/20 ===")
            print("YOU HAVE LOST. I told you it was hard.")


if __name__ == "__main__":
    main()