import random
guesses = []
print("H A N G M A N")

def random_choice():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(word_list)
    return word_list

def player_turn(computer_choice):
    tries = 0
    max_tries = 8
    while tries < max_tries:
        print_word(computer_choice)
        user_guess = input("Input a letter:")
        while not valid_user_guess(user_guess):
            print_word(computer_choice)
            user_guess = input("Input a letter:")
        if not guess_in_word(computer_choice, user_guess):
            tries += 1
        if check_if_won(computer_choice):
            print(f"You guessed the word {computer_choice}!")
            print("You survived!")
            break
    if tries == max_tries:
        print("You lost!")

def valid_user_guess(user_guess):
    if len(user_guess) > 1:
        print("You should input a single letter")
        return False
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if user_guess in letters:
        return True
    else:
        print("It is not an ASCII lowercase letter")
        return False

def guess_in_word(computer_choice, user_guess):
    if user_guess in guesses:
        print("You already typed this letter")
        return True
    if user_guess in computer_choice:
        guesses.append(user_guess)
        return True
    else:
        print("No such letter in the word")
        guesses.append(user_guess)
        return False

def check_if_won(computer_choice):
    for char in computer_choice:
        if char not in guesses:
            return False
    return True

def print_word(computer_choice):
    print()
    for char in computer_choice:
        if char in guesses:
            print(char, end='')
        else:
            print('-', end='')
    print()

def start_game():
    while True:
        user_choice = input("Type 'play' to play the game, 'exit' to quit: ")
        if user_choice == 'play':
            computer_choice = random_choice()
            player_turn(computer_choice)
            break
        elif user_choice == 'exit':
            break
        else:
            continue

start_game()
