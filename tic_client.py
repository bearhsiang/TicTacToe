import socket

name = input(">>> what is your name? ")

s = socket.socket()

server_ip = 'localhost'
server_port = 12345

s.connect((server_ip, server_port))
s.sendall(name.encode())
print(s.recv(1024).decode())
s.sendall('ok'.encode())

while True:
    print(s.recv(1024).decode())
    c = input(">>> place your sign: ")
    s.sendall(c.encode())
