'''12.5 Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.'''

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

data = mysock.recv(512)
header = data.decode()
header_end = header.find('\r\n\r\n') + 4

print(header[header_end:])

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
