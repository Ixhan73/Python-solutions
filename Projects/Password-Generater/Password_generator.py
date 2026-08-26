import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation


while True:

    try:
        chosen_length = int(input("Enter password length(>7): "))
        if chosen_length < 8:
            print("Please enter a greater length.")
            continue

    except ValueError:
        print("Invalid Input!")
        continue


    password = ''.join(secrets.choice(characters) for _ in range(chosen_length))

    print(f"Generated password: {password}")
    break