import random
import sys
import database

accounts = {}


def menu():
    """
    User choices include:
        1. Create an account
        2. Log into account
        0. Exit
    :return customer_choice:
    """
    while True:
        customer_choice = int(input("1. Create an account\n"
                                    "2. Log into account\n"
                                    "0. Exit\n"))
        if customer_choice == 1:
            create_account()
        elif customer_choice == 2:
            log_into_account()
        elif customer_choice == 0:
            print("Bye!")
            break
        else:
            print("Invalid input")


def create_account():
    card_number = set_card_number()
    PIN = set_PIN()
    store_account(card_number, PIN)
    print(f"Your card has been created\n"
          f"Your card number:\n"
          f"{card_number}\n"
          f"Your card PIN:\n"
          f"{PIN}")


def store_account(card_number, PIN):
    global accounts
    accounts[card_number] = PIN
    cur = conn.cursor()
    cur.execute(f"INSERT INTO card VALUES (NULL, {card_number}, {PIN}, 0);")
    conn.commit()


def set_card_number():
    IIN = 400000
    account_number, checksum = set_account_number()
    card_number = f'{IIN}{account_number}{checksum}'
    return card_number


def set_account_number():
    IIN = str(400000)
    account_number = str(random.randint(100000000, 999999999))
    account_list = list(IIN) + list(account_number)
    account_list = [int(x) for x in account_list]
    total = 0
    luhn_list = []
    for index, value in enumerate(account_list, start=1):
        if index % 2 == 1:
            value *= 2

        if value > 9:
            value -= 9

        total += value

        luhn_list.append(value)

    result = total % 10
    if result == 0:
        checksum = str(0)
    else:
        checksum = str(10 - result)
    return account_number, checksum


def set_PIN():
    return str(random.randint(1000, 9999))


def log_into_account():
    input_card_number = input("Enter your card number:\n")
    input_PIN = input("Enter your PIN:\n")
    while not valid_db_account(input_card_number) or not valid_db_PIN(input_PIN):
        print("Wrong card number or PIN!")
        break
    else:
        print("You have successfully logged in!\n")
        login_actions(input_card_number, input_PIN)


def valid_db_account(card_number):
    cur = conn.cursor()
    cur.execute(f"SELECT number FROM card WHERE number = {card_number}")
    if cur.fetchone() is None:
        return False
    else:
        return True

def valid_db_PIN(PIN):
    cur = conn.cursor()
    cur.execute(f"SELECT number FROM card WHERE pin = {PIN}")
    if cur.fetchone() is None:
        return False
    else:
        return True

def login_actions(card_number, PIN):
    print()
    while True:
        user_choice = int(input("1. Balance\n"
                                "2. Add income\n"
                                "3. Do transfer\n"
                                "4. Close account\n"
                                "5. Log out\n"
                                "0. Exit\n"))
        if user_choice == 1:
            balance = check_db_balance(card_number, PIN)
            print(f"Balance: {balance}\n")
        elif user_choice == 2:
            add_income(card_number, PIN)
        elif user_choice == 3:
            do_transfer(card_number, PIN)
        elif user_choice == 4:
            close_account(card_number, PIN)
        elif user_choice == 5:
            print("You have successfully logged out!")
            break
        else:
            sys.exit()

def add_income(card_number, PIN):
    income = int(input("Enter income: \n"))
    update_balance(card_number, income, True)
    print("Income was added!")

def do_transfer(card_number, PIN):
    transfer_account = input("Enter card number: \n")
    if transfer_account == card_number:
        print("You can't transfer money to the same account!")
        return
    if not check_luhn_algorithm(transfer_account):
        print("Probably you made a mistake in the card number. Please try again!")
        return
    if not valid_db_account(transfer_account):
        print("Such a card does not exist.")
        return
    amount = int(input("Enter how much money you want to transfer:\n"))
    balance = check_db_balance(card_number, PIN)
    if balance >= amount:
        update_balance(card_number, amount, False)
        update_balance(transfer_account, amount, True)
        print("Success!")
    else:
        print("Not enough money!")

def check_luhn_algorithm(account):
    account_list = [int(x) for x in account]
    new_account_list = account_list[0:-1]
    total = 0
    luhn_list = []
    for index, value in enumerate(new_account_list, start=1):
        if index % 2 == 1:
            value *= 2

        if value > 9:
            value -= 9

        total += value

        luhn_list.append(value)

    result = total % 10
    if result == 0:
        checksum = 0
    else:
        checksum = 10 - result
    if checksum == account_list[-1]:
        return True
    return False

def update_balance(card_number, amount, increase):
    if not increase:
        amount *= -1
    cur = conn.cursor()
    cur.execute(f"UPDATE card SET balance = balance + {amount} WHERE number = {card_number}")
    conn.commit()

def close_account(card_number, PIN):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM card WHERE number = {card_number} AND pin = {PIN}")
    conn.commit()
    print("The account has been closed!")

def check_db_balance(card_number, PIN):
    cur = conn.cursor()
    cur.execute(f"SELECT balance FROM card WHERE number = {card_number} AND pin = {PIN}")
    balance = cur.fetchone()[0]
    conn.commit()
    # print(f"Balance: {balance}\n")
    return balance


db = "card.s3db"
conn = database.create_connection(db)
database.create_table(conn)
menu()
