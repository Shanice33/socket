from socket import *

HOST='localhost'
PORT=9999
BUFSIZ=1024
ADDR=(HOST,PORT)

udpClnSock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input('>')
    if not data:
        break
    udpClnSock.sendto(data.encode('utf-8'),ADDR)
    data,addr=udpClnSock.recvfrom(BUFSIZ)
    print(addr,data.decode())