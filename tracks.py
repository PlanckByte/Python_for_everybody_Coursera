import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

# Create the tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
handle = open('tracks.csv')

# Process each line from the CSV
# Format: Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Genre
for line in handle:
    line = line.strip()  # Remove leading/trailing spaces
    pieces = line.split(',')  # Split into parts
    if len(pieces) < 7:  # Ensure there are at least 7 columns
        continue

    # Assign variables to parts
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # Insert artist if not already present
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,)) #δινει αυτοματα και id γιατι ετσι το χω ορισει πιο πανω.
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0] #το id toy pinaka Artist  = artist_id gia epomenoys pinakes

    # Insert genre if not already present
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert album if not already present
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Insert or replace track information
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count))

# Commit the changes to the database
conn.commit()

# Query the database and fetch results
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track 
    JOIN Genre ON Track.genre_id = Genre.id
    JOIN Album ON Track.album_id = Album.id
    JOIN Artist ON Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 10''')
results = cur.fetchall()
print(results) # List of tuples
# Close the cursor and connection
cur.close()
conn.close()