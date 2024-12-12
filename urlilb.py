import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1')
raw = fhand.read()
print(raw)