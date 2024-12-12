import urllib.request
import xml.etree.ElementTree as ET
nums = []
integer =[]

url = input("Enter URL:")
sample = urllib.request.urlopen(url)
data = sample.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for result in counts:
    number = result.text
    nums.append(number)
integer = [int(item) for item in nums]    
print(integer)
total = sum(integer)
print(total)           
