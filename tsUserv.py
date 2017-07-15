from socket import *
from time import ctime

HOST=''
PORT=9999
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("...waiting for message")
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    if not data:
        break
    udpSerSock.sendto(b'[%s]%s'%(ctime().encode('utf-8'),data),addr)
    print('...received from and returned to:',addr)
udpSerSock.close()
