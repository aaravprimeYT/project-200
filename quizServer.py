import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipAddress = "127.0.0.1"

port = 5000

server.bind(ipAddress,port)
server.listen()

listOfClients = []

questions = [
    "Where is the state Utah? \n a.America\n b.Syria\n c.England\n d.Dubai"
    "What does N stand for in science? \n a.Sodium\n b. Nickel\n c.Newton\n d.Nitrogen"
    "What is the Italian word for PIE? \n a.Mozzarella\n b.Pasty\n c.Patty\n d.Pizza"]

def get_random_question_answer(connection):
    random_index = random.randint(0,len(questions) -1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    connection.send(random_question.encode("utf-8"))
    return random_index,random_question,random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(connection):
    score = 0
    connection.send("Welcome to this quiz game!".encode("utf-8"))
    connection.send("You will receive a question, The answer to that question will be one of a,b,c or d\n".encode("utf-8"))
    connection.send("Good Luck!".encode("utf-8"))
    index,question,answer = get_random_question_answer(connection)
    
    while True:
        try:
            message = connection.recv(2048).decode("utf-8")
            if message: 
                if message.lower() == answer:
                    score += 1
                    connection.send(f"Bravo! Your score is {score}\n\n".encode("utf-8"))
                else:
                    connection.send("Incorrect Answer! Better luck next time!\n\n".encode("utf-8"))
                remove_question(index)
                index,question,answer = get_random_question_answer(connection)
            else:
                remove(connection)
        except:
            continue

while True:
    connection,address = server.accept()
    listOfClients.append(connection)
    print(address[0] + "connected")
    newThread = Thread(target= clientthread,args=(connection,address))
    newThread.start()
