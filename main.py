
import socket

client=socket.socket()

client.connect(('localhost',9000))
client.send('hi'.encode('utf-8'))
client.close()