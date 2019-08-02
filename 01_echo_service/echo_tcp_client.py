import socket

port = 5890
buff_size = 1024

client_socket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)

server_addr = (socket.gethostname(), port)
client_socket.connect(server_addr)

client_socket.send(b'Hello, there')

data = client_socket.recv(buff_size)
print(f'received data: {data}')

client_socket.close()