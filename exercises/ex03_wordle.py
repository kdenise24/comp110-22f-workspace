"""EX03 - Structured Wordle"""
__author__ = "730566062"

def contains_char(str_input: str, searched_for: str) -> bool:
    """returns a true or false is the single character string is found in the string of any length"""
    assert len(searched_for) == 1
    i: int = 0
    while i < len(str_input):
        if str_input[i] == searched_for:
            return True
        i = i + 1
    return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(secret: str, guess: str) -> str:
    """returns a string of emojis corresponding with the correctness of guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            emoji = emoji + GREEN_BOX  
        else:
            if contains_char(secret, guess[i]):
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji

def input_guess(expected_length: int) -> str:
    """takes the input and insures that the input is the right length"""
    word_input: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(word_input) > expected_length:
        word_input = input("That wasn't " + str(expected_length) +" chars! Try again: ")
    while len(word_input) < expected_length:
        word_input = input("That wasn't " + str(expected_length) +" chars! Try again: ")
    return word_input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    numberof_turns: int = 1
    incorrect_letter: bool = False
    while not incorrect_letter and numberof_turns < 6:
        print("=== Turn " + str(numberof_turns) + "/6 ===")
        player_guess: str = input_guess(5)
        emojis: str = emojified(player_guess, secret_word)
        if secret_word == player_guess:
            print(emojis)
            print("You won in " + str(numberof_turns) + "/6 turns!")
            incorrect_letter = True
        else:
            if incorrect_letter is True:
                print("X/6 - Sorry, try again tomorrow!")
            else:
                print(emojis)
        numberof_turns = numberof_turns + 1

if __name__ == "__main__":
    main()

