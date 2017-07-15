import ftplib
import os
import socket

HOST='localhost'
DIRN='f:/share'
FILE='ss.txt'

def main():
    try:
        f=ftplib.FTP(HOST)
    except(socket.error,socket.gaierror) as e:
        print('error:cannot reach "%s"'%HOST)
        return
    print('***Connected to host "%s"'%HOST)
    print(f.getwelcome())

    try:
        f.login('shanice','ss123')
    except ftplib.error_perm:
        print('error:cannot login anonymously')
        f.quit()
        return
    print('*** logged ')

    try:
        print(f.pwd())
        list = f.nlst()  # 获得目录列表
        for name in list:
            print(name)
        #f.mkd('f:/ss')
        f.cwd('f:/share')
    except ftplib.error_perm:
        print('error:cannot CD to "%s"'%DIRN)
        f.quit()
        return
    print('*** changed to "%s" folder'%DIRN)

    try:
        f.retrbinary('RETR %s'%FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print('error:cannot read file "%s"'%FILE)
        os.unlink(FILE)
    else:
        print('*** download "%s" to CWD'%FILE)
    f.quit()

if __name__=='__main__':
    main()

