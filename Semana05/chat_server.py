#!/usr/bin/python3

import sys
import socket
import threading

if len(sys.argv) < 2:
    sys.exit('Missing arguments')

port = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(100)

clients_conn = []


def connection(conn):
    try:
        print('Waiting for username...')
        username = conn.recv(16)
        username = username.decode()
        print(f'Username received: {username}\n')

        print('Sending welcome...')
        welcome = f'Welcome to this chatroom {username}!'
        conn.send(welcome.encode())
        print('Welcome sent\n')

        while True:
            print('Waiting for message...')
            message = conn.recv(2048)
            message = message.decode()

            if not message:
                break

            print(f'Message received: {message}\n')

            message = f'<{username}> {message}'

            for client_conn in clients_conn:
                if client_conn != conn:
                    client_conn.send(message.encode())
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('Closing connection')
        clients_conn.remove(conn)
        conn.close()


while True:
    print('Waiting for an incoming connection...')
    conn, addr = server.accept()
    print(f'Connected with {addr[1]}\n')

    clients_conn.append(conn)

    thread = threading.Thread(target=connection, args=(conn,))
    thread.start()
