import socket

print("Creating socket....")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("DONE...")
print("Connect remote host....")
s.connect(("www.baidu.com",80))
print("DONE....")