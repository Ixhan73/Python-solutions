def set_difficulty(difficulty):
    if difficulty == '1':
        max_length = 50
        limit = 8

    elif difficulty == '2':
        max_length = 100
        limit = 10

    elif difficulty == '3':
        max_length = 200
        limit = 12

    else:
        print("\nPlease enter from 1-3!\n")
        return None

    return max_length, limit