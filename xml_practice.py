#xml practice
import xml.etree.ElementTree as ET
fhand = open('xml_data.xml')
tree =ET.parse(fhand)
rt = tree.getroot()
print(rt.tag)
print(rt[1][0].text)
first = rt.find('country').attrib
for country in rt.findall('country'):
    name = country.get('name')
    gdppc = country.find('gdppc').text
print(first)
print(name)
print(gdppc)



