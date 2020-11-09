"""
A dictionary that contains a list containing the required amount of:
    water, milk, coffee beans, cups, and cost
"""
coffee_types = [
    {
        'coffee_type': 'espresso',
        'coffee_mapping': 1,
        'ingredients': {
            'water': 250,
            'milk': 0,
            'coffee_beans': 16,
            'cups': 1,
        },
        'money': 4,
    },
    {
        'coffee_type': 'latte',
        'coffee_mapping': 2,
        'ingredients': {
            'water': 350,
            'milk': 75,
            'coffee_beans': 20,
            'cups': 1,
        },
        'money': 7,
    },
    {
        'coffee_type': 'cappuccino',
        'coffee_mapping': 3,
        'ingredients': {
            'water': 200,
            'milk': 100,
            'coffee_beans': 12,
            'cups': 1,
        },
        'money': 6,
    }
]

"""
A dictionary that contains a list.
    The first list element is the quantity currently in the machine
    The second element contains the unit measurement
"""
machine = {
    'ingredients': {
        'water': [400, 'ml'],
        'milk': [540, 'ml'],
        'coffee_beans': [120, 'g'],
        'cups': [9, ''],
    },
    'money': 550
}


def read_input():
    """
    Requests user input to replenish ingredients in machine
    Adds new ingredients to existing machine ingredients
    """
    choice = input('Write action (buy, fill, take, remaining, exit):\n')
    if choice != 'exit':
        valid_input(choice)


def valid_input(choice):
    if choice == 'buy':
        buy()
    elif choice == 'fill':
        fill()
    elif choice == 'take':
        take()
    elif choice == 'remaining':
        print_machine_ingredients()
    else:
        print('Invalid input')
    read_input()


def buy():
    """
    Asks user to input which type of coffee they would like to buy
    Subtracts required ingredients from current machine ingredients
    """
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino ')
    if choice != 'back':
        choice = int(choice)
        [coffee_type] = filter(lambda x: choice == x['coffee_mapping'], coffee_types)
        can_make_coffee = False
        for key, quantity in coffee_type['ingredients'].items():
            if machine['ingredients'][key][0] >= quantity:
                can_make_coffee = True
            else:
                tracker = key
                break
        if can_make_coffee:
            print('I have enough resources, making you a coffee!')
            for key, quantity in coffee_type['ingredients'].items():
                machine['ingredients'][key][0] -= quantity
            machine['money'] += coffee_type['money']
        else:
            print(f'Sorry, not enough {tracker}')


def fill():
    """
    Requests user input to replenish ingredients in machine
    Adds new ingredients to existing machine ingredients
    """
    new_ingredients = {
        'water': int(input('Write how many ml of water to add: ')),
        'milk': int(input('Write how many ml of milk to add: ')),
        'coffee_beans': int(input('Write how many g of coffee beans to add: ')),
        'cups': int(input('Write how many disposable cups to add: ')),
    }
    for key, ingredient in machine['ingredients'].items():
        ingredient[0] += new_ingredients[key]


def take():
    """
    Gives all the money currently in the coffee machine to the user
    Resets the amount of money in the machine to zero
    """
    print(f"I gave you ${machine['money']}\n")
    machine['money'] = 0


def print_machine_ingredients():
    print(f'The coffee machine has:\n'
          f'{machine["ingredients"]["water"][0]} of water\n'
          f'{machine["ingredients"]["milk"][0]} of milk\n'
          f'{machine["ingredients"]["coffee_beans"][0]} of coffee beans\n'
          f'{machine["ingredients"]["cups"][0]} of disposable cups\n'
          f'{machine["money"]} of money\n')


read_input()
