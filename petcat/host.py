import socket
host = "127.0.0.1"
port = 12345
ss = socket.socket()
ss.bind((host,port))
ss.listen()
cs, addr = server.accept()
print ("Connection from: " + str(addr))
while True:
   data = cs.recv(1024).decode()
   if not data:
      break
   print ("from connected user: " + str(data))
   print ("Received from User: " + str(data))
   data = input("type message: ")
   conn.send(data.encode())
cs.close()