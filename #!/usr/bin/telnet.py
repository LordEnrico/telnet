#!/usr/bin/env python3

import socket

# Read "distributed echo server" as "(distributed echo) server". The "server"
# is not "distributed" but the echos are "distributed" to every connected
# client.

# Connect to the server with `telnet $HOSTNAME 5000`.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind((socket.gethostname(), 5000))
server.listen(5)

connections = []

while True:
    try:
        connection, address = server.accept()
        connection.setblocking(False)
        connections.append(connection)
    except BlockingIOError:
        pass

    for connection in connections:
        try:
            message = connection.recv(4096)
        except BlockingIOError:
            continue

        for connection in connections:
            connection.send(message)
