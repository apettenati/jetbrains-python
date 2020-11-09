import random

winner = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
valid_input = [ '!quit', '!rating', *winner.keys()]


def check_rating():
    print(f'Your rating: {rating}')


def print_win_condition(user_guess):
    global rating
    # dictionary of guesses and winners against that choice
    computer_guess = random.choice(list(winner.keys()))
    if user_guess == computer_guess:
        print("There is a draw (" + user_guess + ")")
        rating += 50
    elif user_guess == winner[computer_guess]:
        print("Well done. The computer chose " + computer_guess + " and failed")
        rating += 100
    else:
        print("Sorry but the computer chose " + computer_guess)


def play_RPS():
    user_guess = input()
    while user_guess != "!exit":
        if user_guess not in valid_input:
            print("Invalid input")
        if user_guess == '!rating':
            check_rating()
        if user_guess in winner.keys():
            print_win_condition(user_guess)
        user_guess = input()
    else:
        print("Bye!")

# greet user
name = input('Enter your name: ')
print(f'Hello, {name}')
# read a file
rating_file = open('rating.txt')
# get score
rating = 0
for line in rating_file:
    variable = line.split()
    prior_player = variable[0]
    if name == variable[0]:
        rating = int(variable[1])
        break
play_RPS()
rating_file.close()

