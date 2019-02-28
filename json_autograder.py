
import urllib.request
import urllib.parse
import urllib.error
import json
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

info = json.loads(html)

print('Retreiving', count, 'characters')
print('User count:', len(info))

newlst = []
for item in info['comments']:
    count = item['count']
    newlst.append(count)

print('Sum:', sum(newlst))
