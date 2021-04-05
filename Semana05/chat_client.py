#!/usr/bin/python3

import sys
import socket
import select

if len(sys.argv) < 4:
    sys.exit('Missing arguments')

host = sys.argv[1]
port = int(sys.argv[2])
username = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('Connecting to the server...')
    client.connect((host, port))
    print('Connected\n')

    print('Sending username...')
    client.send(username.encode())
    print('Username sent\n')

    print('Waiting for welcome...')
    welcome = client.recv(64)
    print(f'Welcome received: {welcome.decode()}\n')

    while True:
        read_list, write_list, error_list = select.select(
            [sys.stdin, client], [], [])

        if client in read_list:
            message = client.recv(2048)
            message = message.decode()

            if not message:
                break

            print(message)
        else:
            message = sys.stdin.readline().replace('\n', '')
            client.send(message.encode())
            print(f'<You> {message}')
except Exception as e:
    print(f'Error: {e}')
finally:
    print('Closing connection')
    client.close()