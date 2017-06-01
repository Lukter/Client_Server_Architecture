# README CLIENT-SERVER ARCHITECTURE

This repository has:
* *Client*
* *Server*

## Client-Server Architecture
This project consists in the implementation of a server-client architecture using TCP sockets. This solution use threads and TCP socket.

### Client features
1. Client increments a number every 500 ms when connected with the server. This number is received through the server. By default, the increment is 1.
2. A random even/odd number request is made by client. This request is made every 3-5 seconds.
   The received number is the new increment value.
3. There is very simple command to connect or shutdown the client. If the input is 'c', the client will connect and with input 's' the client will be shutdown.

### Server features
1. Server computes a random even number within range 0-99.
2. Server computes a random odd nuber within rang 0-99.
3. Save every message in a log file.

## Notes

### General
1. Its tried to use only thread-safe functions.
2. It was used processes to differentiate client and server. The real number of clients is limited by available memory.
 
### Client
1. Client has a ID. The ID is used by server to register the client.
2.  This ID is a random number within range 0-10000. So, theoretically, it's possible to register 10001 clients.
3. The calculator function don't increment the number exactly every 500 ms. It is assumed that all operations occur instantly.
4. Any message sent use a sentinel. This sentinel is characterized by " " (blank space).
5. Its used this sentinel because client is faster than server, therefore, it's possible to have more than one message in buffer and server need to split the buffer data.

### Server
1. Server's IP is the localhost IP.
2. The port used is defined 2004. It's used a four-digit numbers to avoid conflicts.
3. Server mantain 3 list with: Client's ID, last odd/even number generated and last client calculated number.
4. Every saved messaged is save in a file named "server.log".
