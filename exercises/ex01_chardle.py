"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730566062"

Instances: int = 0

five_character_word: str = input ("Enter a 5-character word: ")

if len(five_character_word) > 5:
    print("Error: Word must contain 5 character")
    print(exit())
if len(five_character_word) < 5:
    print("Error: Word must contain 5 character")
    print(exit())

single_character: str = input ("Enter a single character: ")
if len(single_character) > 1:
    print("Error: Character must be a single character.")
    print(exit())
if len(five_character_word) < 1:
    print("Error: Character must be a single character.")
    print(exit())

print("Searching for " + single_character + " in " + five_character_word)

if single_character == five_character_word[0]:
    Instances = Instances + 1
    print(single_character + " found at index 0")
if single_character == five_character_word[1]:
    Instances = Instances + 1
    print(single_character + " found at index 1")
if single_character == five_character_word[2]:
    Instances = Instances + 1
    print(single_character + " found at index 2")
if single_character == five_character_word[3]:
    Instances = Instances + 1
    print(single_character + " found at index 3")
if single_character == five_character_word[4]:
    Instances = Instances + 1
    print(single_character + " found at index 4")



if Instances > 1:
    print((str(Instances)) + " instances of " + single_character + " found in " + five_character_word)
if Instances == 0:
    print ("No instances of " + single_character + " found in " + five_character_word)
if Instances == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
