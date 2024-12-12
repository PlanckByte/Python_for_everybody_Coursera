import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
#creating the table or droping it first if it exist
cur.execute('DROP TABLE IF EXISTS Mailbox')
cur.execute('CREATE TABLE Mailbox (email TEXT, count INTEGER)')

fname = input ('Enter File:')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh: 
    if not line.startswith('From:'): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Mailbox WHERE email=?', (email,)) #query to see for every email the count
    row = cur.fetchone() #fetches the result
    if row is None:
        cur.execute('INSERT INTO Mailbox(email,count) VALUES(?,1)', (email,)) #if it doesnot exist add 1
    else:
        cur.execute('UPDATE Mailbox SET count = count+1 WHERE email=?', (email,)) #if it exists update
    conn.commit()#write the changes to the hard drive basically
    
print('Mailbox:')
cur.execute('SELECT email,count FROM MAILBOX ORDER BY count DESC LIMIT 10') 
for row in cur:
    print(row)
    
cur.close()    


    