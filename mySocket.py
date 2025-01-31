import socket
# connecting two nodes on a network to communicate with each other. 
# One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection.
# create a new socket object
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#A server has a bind() method which binds it to a specific IP and port so that it can listen to incoming requests on that IP and port.
mySocket.bind(('localhost', 8080))

#Calling listen() makes a socket ready for accepting connections.
mySocket.listen(5)

while True:
    print("waiting for a connection...")
    (recvSocket, address) = mySocket.accept()
    print("yay http request has been received!!")
    print(recvSocket.recv(1024)) #receive the data which is coming either from a server or from a client
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World everyone!!</h1></body></html> \r\n", 'utf=8'))
    recvSocket.close()