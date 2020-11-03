import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = socket.getservbyname('http','tcp')
print("connecting to remote host on port %d" %port)
s.connect(("www.baidu.com",port))
print("done")
print("Connected from",s.getsockname())
print("Connected to",s.getpeername())