import socket      # Import socket module
my_socket = socket.socket()      # Create a socket object
my_host = "127.0.0.1"
my_port = 6969# Store a port for your service.
my_socket.connect((my_host, my_port))
print (my_socket.recv(1024))
my_socket.close