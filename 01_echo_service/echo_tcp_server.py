#!/usr/bin/env python

import socket

port = 5890
queue_length = 5
buff_size = 1024

# tcp socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = (socket.gethostname(), port)
server_socket.bind(server_addr)

server_socket.listen(queue_length)

# the connection for the connected client
conn, client_addr = server_socket.accept()
print(f'Connection established from {client_addr}')

data = conn.recv(buff_size)

# send the data back to the client
conn.send(data)

conn.close()

# close the socket that listens for new connections
server_socket.close()