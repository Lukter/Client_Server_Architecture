import socket
import time
from random import randint
from threading import Thread


class Client(Thread):
    def __init__(self, tcpClientA, flag_connection):
        Thread.__init__(self)
        self.tcpClientA = tcpClientA
        self.flag_connection = flag_connection

    def run(self):
        try:
            self.tcpClientA.connect((host, port))
            self.tcpClientA.send(str(ID))
            number = self.tcpClientA.recv(1024)
            increment = 1
            if self.flag_connection is False:
                self.flag_connection = True
            while True:
                t_end = time.time() + randint(3, 5)
                while time.time() < t_end:
                    number = calculator(int(number), int(increment))
                    self.tcpClientA.send(str(number) + " ")
                self.tcpClientA.send(requisition[randint(0, 1)] + " ")
                increment = self.tcpClientA.recv(1024)
        except:
            print "Client is OFFLINE"
            threads.remove(newthread)
            return


def calculator(number, increment):
    number = number + increment
    time.sleep(0.5)
    return number


requisition = ['odd', 'even']
ID = randint(0, 10000)
host = socket.gethostname()
port = 2004
BUFFER_SIZE = 20
flag_connection = False
threads = []
print "c - connect to server"
print "s - shutdown client"
print "exit - exit client terminal\n\n"
while True:
    command = raw_input("What do you want to do? \n")
    if command == 'c':
        if not threads:
            tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            newthread = Client(tcpClientA, flag_connection)
            newthread.start()
            threads.append(newthread)
        else:
            print "Client already running!"
    if command == 's':
        if not threads:
            print "Client isn't running!"
        else:
            tcpClientA.close()
    if command == 'exit':
        tcpClientA.close()
        exit()
