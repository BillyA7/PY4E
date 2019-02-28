
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieiving', url)
html = urllib.request.urlopen(url, context=ctx).read()
count = 0
for char in html:
    count += 1
tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
print('Retreiving', count, 'characters')
print('User count:', len(lst))

newlst = []
for item in lst:
    count = item.find('count').text
    newlst.append(int(count))

print('Sum:', sum(newlst))
