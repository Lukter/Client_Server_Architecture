import socket
import time
from random import randint
from threading import Thread


class Client(Thread):
    def __init__(self, c_socket, register):
        Thread.__init__(self)
        self.c_socket = c_socket
        self.register = register

    def run(self):
        try:
            self.c_socket.connect((host, port))
            self.c_socket.send(str(ID))
            number = self.c_socket.recv(BUFFER_SIZE)
            increment = 1
            if self.register is False:
                self.register = True
            while True:
                t_end = time.time() + randint(3, 5)
                while time.time() < t_end:
                    number = calculator(int(number), int(increment))
                    self.c_socket.send(str(number) + " ")
                self.c_socket.send(requisition[randint(0, 1)] + " ")
                increment = self.c_socket.recv(BUFFER_SIZE)
        except:
            print "Client is OFFLINE"
            threads.remove(client_thread)
            return


def calculator(number, increment):
    number = number + increment
    time.sleep(0.5)
    return number


requisition = ['odd', 'even']
ID = randint(0, 10000)
host = socket.gethostname()
port = 2004
BUFFER_SIZE = 1024
register = False
threads = []
print "c - connect to server"
print "s - shutdown client"
print "exit - exit client terminal\n\n"
while True:
    command = raw_input("What do you want to do? \n")
    if command == 'c':
        if not threads:
            c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_thread = Client(c_socket, register)
            client_thread.start()
            threads.append(client_thread)
        else:
            print "Client already running!"
    if command == 's':
        if not threads:
            print "Client isn't running!"
        else:
            c_socket.close()
    if command == 'exit':
        c_socket.close()
        exit()
