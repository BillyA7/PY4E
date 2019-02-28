'''12.3 Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.'''

import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

char = 0
for letter in line.decode():
    if char >= 3000:
        break
    else:
        char += 1

print('Characters:', char)
