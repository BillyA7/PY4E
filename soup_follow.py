import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
counts = int(input('Enter Count: '))
pos = int(input('Enter Position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = 0
print('Retrieving: ' + url)
# Retrieve all of the anchor tags
tags = soup('a')
lst = []
for tag in tags:
    lst.append(tag.get('href', None))

while count < counts - 1:
    new_url = lst[pos - 1]
    html_open = urllib.request.urlopen(new_url, context=ctx).read()
    parser = BeautifulSoup(html_open, 'html.parser')
    new_tag = parser('a')
    lst = []
    for tag in new_tag:
        lst.append(tag.get('href', None))
    print('Retrieving: ' + lst[pos - 1])
    count += 1
