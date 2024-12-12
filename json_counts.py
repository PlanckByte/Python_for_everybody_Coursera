import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location:")
data = urllib.request.urlopen(url, context = ctx).read()
info = json.loads(data)
info = info['comments'] #To go to the specific key of the Json and search under that
total = 0
for item in info: #every"item" is another dictionary within the list of "comments" which a key in the whole Json
    total = total + int(item['count'])
    
print("Sum:",total)
   
