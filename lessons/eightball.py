from random import randint

question: str = input("ask a yes or no question...")
response: int = randint(0, 2)

if response == 0:
    print("yes def")
elif response == 1:
        print("ask again later")
else:
        print("no")