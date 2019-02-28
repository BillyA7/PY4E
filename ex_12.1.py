'''12.1 Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    inp = input('Enter Web Address: ')
    site = inp.split('/')
    host = site[2]
    mysock.connect((host, 80))
    cmd = 'GET '.encode() + inp.encode() + ' HTTP/1.0\r\n\r\n'.encode()
except IndexError:
    print('Incorrect URL entered.')
    quit()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
