# README CLIENT-SERVER ARCHITECTURE

This repository has:
* *Client*
* *Server*

## Client-Server Architecture
This project consists in the implementation of a server-client architecture using TCP sockets. This solution uses threads and TCP socket.

### Client features
1. Client increments a number every 500 ms when connected with the server. This number is received through the server. By default, the increment is 1.
2. A random even/odd number request is made by client. This request is made every 3-5 seconds.
   The received number is the new increment value.
3. There is a very simple command to connect or shutdown the client. If the input is 'c', the client will connect and with input 's' the client will be shutdown.

### Server features
1. Server computes a random even number within range 0-99.
2. Server computes a random odd nuber within range 0-99.
3. Saves every message in a log file.

### How to use
1. Open terminal and run server_v10.py
2. Open another terminal and run client_v10.py

## Notes

### General
1. Its tried to use only thread-safe functions.
2. It was used processes to differentiate client and server. The real number of clients is limited by available memory.
 
### Client
1. Client has an ID. The ID is used by server to register the client.
2. This ID is a random number within range 0-10000. So, theoretically, it's possible to register 10001 clients.
3. The calculator function doesn't increment the number exactly every 500 ms. It is assumed that all operations occur instantly.
4. Any message sent uses a sentinel. This sentinel is characterized by " " (blank space).
5. Its used this sentinel because client is faster than server, therefore, it's possible to have more than one message in buffer and server needs to split the buffer data.

### Server
1. Server's IP is the localhost IP.
2. The port used is defined 2004. It's used a four-digit numbers to avoid conflicts.
3. Server mantains 3 list with: Client's ID, last odd/even number generated and last client calculated number.
4. Every saved message is saved in a file named "server.log".
