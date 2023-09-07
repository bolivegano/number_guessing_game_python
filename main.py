import random

play_game = "y"

while play_game == "y":
    answer = random.randint(1, 100)
    try_number = int(input("Guess a number between 1 and 100: "))
    counter = 1

    while try_number != answer:
        if try_number > answer:
            print("Your number is too large.")
        else:
            print("Your number is too small")
        try_number = int(input("Guess again: "))
        counter += 1
    print(f"You got it in {counter} attempt(s)!")
    play_game = input("Continue? (y/n): ")
