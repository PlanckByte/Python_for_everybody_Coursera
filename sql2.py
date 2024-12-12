import sqlite3

conn = sqlite3.connect('email2db.sqlite')
cur = conn.cursor()
#creating the table or droping it first if it exist
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input ('Enter File:')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh: 
    if not line.startswith('From:'): continue
    pieces = line.split()
    email = pieces[1]
    x = email.split("@")
    org = x[1]
    cur.execute('SELECT count FROM Counts WHERE org=?', (org,)) #query to see for every email the count
    row = cur.fetchone() #fetches the result
    if row is None:
        cur.execute('INSERT INTO Counts(org,count) VALUES(?,1)', (org,)) #if it does not exist add 1
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE org=?', (org,)) #if it exists update
conn.commit()#write the changes to the hard drive basically
cur.execute ('SELECT org,count FROM Counts ORDER BY count DESC')   

    
cur.close()    


    