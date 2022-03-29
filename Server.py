import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
print ("Socket successfully created")
port = 1234 
s.bind((socket.gethostname(), port)) 
print ("socket binded to %s" %(port)) 
s.listen(5)
print ("socket is listening") 
while True:
    clientsocket, address = s.accept()
    print (f"Got connection from {address} has been established!!") 
    clientsocket.send("Thank you for connecting".encode()) 
    clientsocket.close()
    break 
