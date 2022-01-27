import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 5000

server.connect((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []

print("Server has started...")

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                remove (clients)
                

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def clientthread(connection, nickname):
    while True:
        try:
            message = connection.recv(2048).decode('utf-8')
            if message:
                print(message)
                broadcast(message, connection)
            else:
                remove_nickname(nickname)
        except:
            continue

def receive(connection,nickname):
    receive_thread = Thread(target=receive)
    receive_thread.start()
    while True:
        try:
            message = connection.recv(2048).decode('utf-8')
            if message:
                print(message)
                broadcast(message, connection)
            else:
                clients.close()
                break
        except:
            continue

def write(nickname):
    write_thread = Thread(target=write)
    write_thread.start()
    while True:
        nickname = input()   
        clients.send(message.encode('utf-8'))



def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    connection, addr = server.accept()
    connection.send('NICKNAME'.encode("utf-8"))
    nickname = connection.recv(2048).decode("utf-8")
    list_of_clients.append(connection)
    nicknames.append(nickname)
    print(nickname + "connected!")
    new_thread = Thread(target= receive,args=(connection,nickname))
    new_thread.start()

