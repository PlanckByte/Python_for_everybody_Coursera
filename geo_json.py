import json
import urllib.request, urllib.parse, urllib.error
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
#Ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location:')
address = address.strip()
parms = dict()
parms['q'] = address
#adding the parameters to the url, encoded
url = serviceurl + urllib.parse.urlencode(parms)
link = urllib.request.urlopen(url, context=ctx)
data = link.read().decode()
print ('Retrieved',len(data),'characters',data[:20].replace('\n',' ')) #debug print to see success connect

try:
    js = json.loads(data)
except:
    js = None

if not js or "features" not in js:
    print('==== Download error ===')
    print(data)
    
if len(js['features']) == 0:
    print('==== Object not found ====')
    print(data)   
        
print(json.dumps(js, indent=4))
plus_code = js['features'][0]['properties']['plus_code']
print(plus_code)
