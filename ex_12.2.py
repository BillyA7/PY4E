'''12.2 Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.'''

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

char = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
    for i in data.decode():
        if char >= 3000:
            break
        else:
            char += 1

print('Characters: ', char)

mysock.close()
