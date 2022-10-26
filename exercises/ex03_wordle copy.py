"""EX03 - Structured Wordle."""
__author__ = "730566062"


def contains_char(str_input: str, searched_for: str) -> bool:
    """Returns a true or false is the single character string is found in the string of any length."""
    assert len(searched_for) == 1
    i: int = 0
    while i < len(str_input):
        if str_input[i] == searched_for:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis corresponding with the correctness of guess."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_str: str = ""
    i: int = 0
    assert(len(guess) == len(secret))
    while i < len(secret):
        if secret[i] == guess[i]:
            emoji_str += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        i += 1
    return emoji_str


def input_guess(expected_length: int) -> str:
    """Takes the input and insures that the input is the right length."""
    word_input: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(word_input) != expected_length:
        word_input = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return word_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    numberof_turns: int = 1
    correct_guess: bool = False
    while not correct_guess and numberof_turns <= 6:
        print("=== Turn " + str(numberof_turns) + "/6 ===")
        player_guess: str = input_guess(len(secret_word))
        emojis: str = emojified(player_guess, secret_word)
        print(emojis)
        if secret_word == player_guess:
            print("You won in " + str(numberof_turns) + "/6 turns!")
            correct_guess = True
        numberof_turns += 1

    if correct_guess is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()