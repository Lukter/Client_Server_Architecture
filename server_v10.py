import socket
import logging
from threading import Thread
from random import randint


class ClientThread(Thread):
    def __init__(self, ip, port, socket, ID):
        Thread.__init__(self)
        self.ID = ID
        self.ip = ip
        self.socket = socket
        self.port = port

    def run(self):
        while True:
            data = self.socket.recv(BUFFER_SIZE)
            if data == '':
                print "Client " + str(self.ID) + " disconnected"
                logger.info("Client " + str(self.ID) + " disconnected")
                break
            print "Value calculated by client " + str(self.ID) + " :" + data
            logger.info("Value calculated by client "
                        + str(self.ID) + " :" + data)
            messages = data.count(" ") - 1
            select = data.split(" ")
            while messages >= 0:
                if select[messages] == 'odd':
                    print ("Client: " + str(self.ID)
                           + "made an odd number requisition")
                    logger.info("Client " + str(self.ID)
                                + " made an odd number requisition")
                    odd_number = client_thread.odd()
                    client_thread.store(odd_number, 1)
                    self.socket.send(str(odd_number))
                    print ("Odd number sent to client: "
                           + str(self.ID) + " : " + str(odd_number))
                    logger.info("Odd number sent to client "
                                + str(self.ID) + ": " + str(odd_number))
                if select[messages] == 'even':
                    print ("Client: " + str(self.ID)
                           + " made an even number requisition")
                    logger.info("Client " + str(ID)
                                + " made an even number requisition")
                    even_number = client_thread.even()
                    client_thread.store(even_number, 1)
                    self.socket.send(str(even_number))
                    print ("Even number sent to client " + str(self.ID)
                           + " : " + str(even_number))
                    logger.info("Even number sent to client "
                                + str(self.ID) + " : " + str(even_number))
                if select[messages] != 'odd' and select[messages] != 'even':
                    client_thread.store(select[messages], 0)
                messages = messages - 1
            s_socket.listen(4)

    def odd(self):
        number = randint(0, 98)
        select = number % 2
        if select == 0:
            return number+1
        else:
            return number

    def even(self):
        number = randint(1, 99)
        select = number % 2
        if select == 0:
            return number
        else:
            return number-1

    def store(self, item, signal): #0 - store number | 1 - store counter
        if signal == 0:
            list_calc.insert(list_client.index(ID), item)
        if signal == 1:
            list_counter.insert(list_client.index(ID), item)
        return 0


def log():
    logger = logging.getLogger('server')
    hdlr = logging.FileHandler('server.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    return logger


def connect(key):
    if key in list_client:
        print "Client already registered"
        logger.info("Client already registered")
        print ("Client ID: " + str(key) + "Client last calculated number: "
               + str(list_calc[list_client.index(key)]))
        logger.info("Client ID: " + str(key) + "Client last calculated number: "
                    + str(list_calc[list_client.index(key)]))
        return list_calc[list_client.index(key)]
    else:
        print "New Client"
        print "Registering..."
        list_client.append(key)
        list_counter.append(1)
        list_calc.append(0)
        print "Client registered with ID: ", key,  "and number: 0"
        logger.info("Client registered with ID: "
                    + str(key) + "and number: 0")
        return 0


threads = []
list_client = []
list_counter = []
list_calc = []
TCP_IP = '0.0.0.0'
TCP_PORT = 2004
BUFFER_SIZE = 1024
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_socket.bind((TCP_IP, TCP_PORT))
logger = log()
print "SERVER ONLINE"
logger.info("Server Online")
while True:
    print "Waiting for new connections"
    s_socket.listen(4)
    (conn, (ip, port)) = s_socket.accept()
    port = str(port)
    print "Connection accepted with port: " + port
    logger.info("Connection accepted with port: " + port)
    ID = conn.recv(BUFFER_SIZE)
    logger.info("Received ID from client: " + ID)
    conn.send(str(connect(ID)))
    print "Counter sent to client with ID: " + ID
    logger.info("Counter sent to client " + ID)
    client_thread = ClientThread(ip, port, conn, ID)
    client_thread.start()
    threads.append(client_thread)
