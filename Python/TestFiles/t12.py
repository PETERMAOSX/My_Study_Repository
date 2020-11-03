import socket


print("Creating socket....")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("DONE...")
print("----")
port = socket.getservbyname('http','tcp')
print("Connect remote host.... %d"%port)
s.connect(("www.baidu.com",port))
print("DONE....")
