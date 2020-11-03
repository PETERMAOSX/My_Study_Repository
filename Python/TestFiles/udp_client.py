import socket
host = "localhost"
port = 1024
buf_size = 128
addr = (host,port)
upd_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	data = raw_input('>')
	if not data:
		break
	udp_client.sendto(data,addr)
udp_client.close()

