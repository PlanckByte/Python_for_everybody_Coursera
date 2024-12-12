
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
numbers=[]
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter -')
html= urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
print(tags)
for tag in tags:
    numbers.append((int(tag.contents[0])))
print(numbers)
total=sum(numbers)
print(total)    
    
                   
    