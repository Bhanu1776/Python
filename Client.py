import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1234
s.connect((socket.gethostname(), port))
msg = s.recv(1024)
 
print(msg.decode())
s.close()
