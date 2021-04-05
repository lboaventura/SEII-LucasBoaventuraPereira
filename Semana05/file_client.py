#!/usr/bin/python3

import sys
import socket

if len(sys.argv) < 4:
    sys.exit('Missing arguments')

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('Connecting to the server...')
    client.connect((host, port))
    print('Connected')

    print('Receiving file...')
    with open(filename, 'wb') as file:
        while True:
            data = client.recv(1024)
            file.write(data)

            if not data:
                break
    print('File received')
except Exception as e:
    print(f'Error: {e}')
finally:
    print('Closing connection')
    client.close()
