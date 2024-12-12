import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

meter = 0
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ("Enter URL:")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("a")
position = input('Enter Position:')
position = int(position)
position = position -1
count = input(('Enter count:')) 
count = int(count)

#Loop that goes to the desired position in the tags list and extracts the url and visits it

while count != meter:
    ctx=ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
#We assing the href value to the new url and not the tag[position] directly.IMPORTANT!
    url = tags[position].get('href',None) 
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    meter+=1 

