import socket

game_map = [' '] * 9

def get_choice(p):
    
    while True:
        
        text = draw_map()
        p[0].sendall(text.encode())
        c = p[0].recv(1024).decode()
        c = int(c)
        
        if game_map[c] == ' ':
            break

    return c

def draw_map():
    m = ''
    for i in range(9):
        m += game_map[i]
        if i % 3 == 2:
            m += '\n'
        else:
            m += '|'
    return m

ip = ''
port = 12345


s = socket.socket()
s.bind((ip, port))
s.listen()

p1 = s.accept()
p1_name = p1[0].recv(1024).decode()
print(p1_name)
p2 = s.accept()
p2_name = p2[0].recv(1024).decode()
print(p2_name)

p1[0].sendall('game start! you are O'.encode())
p2[0].sendall('game start! you are X'.encode())
p1[0].recv(1024)
p2[0].recv(1024)

while True:
    c = get_choice(p1)
    game_map[c] = 'O'
    c = get_choice(p2)
    game_map[c] = 'X'




'''
_|_|_
_|_|_
_|_|_
'''