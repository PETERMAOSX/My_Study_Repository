import socket
from threading import Thread
ADDRESS = ('127.0.0.0',8712) #绑定地址
g_socket_server = None #负责监听的socket
g_conn_pool=[] #连接池

def init():
    #初始化
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5) #最大等待数
    print("Server has been Started. waiting for connection.")