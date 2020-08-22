import socket
from threading import Thread


def Communication(conn):
    # 通信循环1
    while 1:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print('Client Data:', data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError:
            break

def Server(ip,post):
    whw_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    whw_server.bind((ip,post))
    whw_server.listen(128)
    # 链接循环
    while 1:
        conn, addr = whw_server.accept()
        #创建线程
        t = Thread(target=Communication,args=(conn,))
        t.start()

if __name__ == '__main__':
    #主线程干Server的工作
    Server('127.0.0.1',9000)