import random

play_game = "y"
start = 1
end = 100
direction = "N"
smallest = start
largest = end

while play_game == "y":
    smallest = start
    largest = end
    print(f"guess a number between {start} and {end}: ")
    try_number = random.randint(start, end)
    print(try_number)
    counter = 0
    direction = "N"

    while direction != "c":
        direction = input("Is it too large? (l), too small?(s), or correct?(c)")
        if direction == "s":
            if try_number > smallest:
                smallest = try_number + 1
            try_number = random.randint(smallest, largest)
            print(try_number)
        if direction == "l":
            if try_number < largest:
                largest = try_number - 1
            try_number = random.randint(smallest, largest)
            print(try_number)
        counter = counter + 1
    print(f"I got it, I tried {counter} times.")
    play_game = input("Continue? (y/n)")
