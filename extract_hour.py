name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
hour_count = dict()
for line in handle:
    line =line.strip()
    if not line.startswith("From"): continue
    words=line.split()
    if len(words) <6 : continue 
    time=words[5]
    hour=time.split(":")[0] 
    hour_count[hour]=hour_count.get(hour,0) + 1
t = list(hour_count.items())
t.sort()
for hour,count in t:
    print(hour,count)
    
    
   
    

    
   
