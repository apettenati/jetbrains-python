import socket
import sys
import logging
import itertools

logging.basicConfig(level=logging.DEBUG, filename='log.log')


def password_generator():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 1
    while True:
        password = itertools.product(chars, repeat=i)
        i += 1
        for elem in password:
            yield ''.join(elem)


def read_password_file():
    with open('C:\\Users\\Amanda\\Google Drive\\python\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt') as f:
        word = f.readline().strip('\n')
        while word:
            password = itertools.product(*([char.upper(), char.lower()] for char in word))
            for elem in password:
                yield ''.join(elem)
            word = f.readline().strip("\n")
            logging.debug(f'new line {word}')


def main():
    args = sys.argv
    with socket.socket() as client_socket:
        hostname = args[1]
        port = int(args[2])
        address = (hostname, port)
        client_socket.connect(address)

        password = read_password_file()
        client_socket.send(next(password).encode())

        response = client_socket.recv(1024).decode()
        while response != "Connection success!":
            pw = next(password)
            client_socket.send(pw.encode())
            response = client_socket.recv(1024).decode()
            logging.debug(response + ', ' + pw)
        print(pw)


main()
