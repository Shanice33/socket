from socket import *
from time import ctime

HOST=''
PORT=9999
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection....")
    SS,addr=tcpSerSock.accept()
    print('connected from:',addr)
    while True:
        data=SS.recv(BUFSIZ)
        if not data:
            break
        SS.send('[%s]%s'%(bytes(ctime(),'utf-8'),data))

        SS.close()
