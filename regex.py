import re
num=[]
fhand = open('actual data.txt')
for line in fhand:
    line=line.rstrip()
    x= re.findall('[0-9]+', line)
    if len (x)>0:  
       num.extend(x)
num = [int(i) for i in num]
s = sum(num)
print (s)



        
   
