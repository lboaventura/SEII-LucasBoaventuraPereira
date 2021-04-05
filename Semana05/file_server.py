#!/usr/bin/python3

import sys
import socket

if len(sys.argv) < 3:
    sys.exit('Missing arguments')

port = int(sys.argv[1])
filename = sys.argv[2]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(1)

while True:
    print('Waiting for an incoming connection...')
    conn, addr = server.accept()
    print(f'Connected with {addr[1]}')

    try:
        with open(filename, 'rb') as file:
            content = file.read()

        print('Sending file...')
        conn.send(content)
        print('File sent')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('Closing connection')
        conn.close()
