#!/usr/bin/python

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

HOST = socket.gethostname()
PORT = 1234
print HOST

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((HOST, PORT))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola, eres de la IP: <h1>" +
                        str(address[0]) +
                        "<h1>y de este puerto: <h1>" +
                        str(address[1]) +
                        "</p>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()

except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
