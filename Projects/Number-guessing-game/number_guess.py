import random
from functions import set_difficulty

play_again = True
levels = ['\n1.Easy', '2.Medium', '3.Hard']

while play_again:
    for level in levels:
        print(level)

    difficulty_level = input("\nChoose difficulty level [1-3]: ")
    settings = set_difficulty(difficulty_level)

    if settings is None:
        continue

    max_length, limit = settings
    secret = random.randint(1, max_length)
    attempts = 0

    while True:

        try:
            guess = int(input(f"\nEnter your guess(1-{max_length}): "))

            if not 1<= guess <= max_length:
                print(f"\nPlease enter between 1-{max_length}\n")
                continue

            attempts += 1

        except ValueError:
            print("\nInvalid Input!\n")
            continue

        if guess == secret:
            print("\nYour guess was right!")
            print(f"Total attempts: {attempts}")

            break

        elif guess < secret:
            print("\tGo higher")

        else:
            print("\tGo lower")

        if attempts >= limit:
            print(f"\nYou've reached {limit}-attempt limit!")
            print(f"The number was {secret}.") 

            break

    while True:
        restart = input("Do you want to restart(y/n): ")

        if restart == 'y':
            play_again = True
            break

        elif restart == 'n':
            play_again = False
            break
        else:
            print("Invalid input!")
            continue