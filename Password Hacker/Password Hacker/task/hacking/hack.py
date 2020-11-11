import socket
import sys

args = sys.argv

# message = input().strip('python hack.py ').split(' ')

with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    message = args[3]
    address = (hostname, port)

    client_socket.connect(address)

    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(response)
