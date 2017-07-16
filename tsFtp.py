import ftplib
import os
import socket

HOST='localhost'
DIRN='share'
FILE=r'ss.txt'   #文件格式

def main():
    try:
        f=ftplib.FTP(HOST)   #和ftp服务器建立连接
    except(socket.error,socket.gaierror) as e:
        print('error:cannot reach "%s"'%HOST)
        return
    print('***Connected to host "%s"'%HOST)
    print(f.getwelcome())

    try:
        f.login('shanice','ss123')  #登陆
    except ftplib.error_perm:
        print('error:cannot login ')
        f.quit()
        return
    print('*** logged ')

    try:
        print(f.pwd())
        list = f.nlst()  # 获得目录列表
        for name in list:
            print(name)
        #f.mkd('ss')
        #f.rmd('ss')
        f.cwd(DIRN)      #切换ftp服务器的工作目录
    except ftplib.error_perm:
        print('error:cannot CD to "%s"'%DIRN)
        f.quit()
        return
    print('*** changed to "%s" folder'%DIRN)

    try:
        f.retrbinary('RETR %s'%FILE,open('s.txt','wb').write)    #从服务器下载文件
    except ftplib.error_perm:
        print('error:cannot read file "%s"'%FILE)
        os.unlink(FILE)
    else:
        print('*** download "%s" from CWD'%FILE)
    f.quit()

if __name__=='__main__':
    main()

