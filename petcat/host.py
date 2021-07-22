import socket
my_socket = socket.socket()      # Create a socket object
# my_host = socket.gethostname()
my_host = "0.0.0.0"
my_port = 6969# Store a port for your service.
my_socket.bind((my_host, my_port))
my_socket.listen(5)      # Now wait for client connection.
while True:
   cl, myaddr = my_socket.accept()     # Establish connection with client.
   print ('Got connection from', myaddr)
   cl.send('Thank you for connecting')
   cl.close()     # Close the connection