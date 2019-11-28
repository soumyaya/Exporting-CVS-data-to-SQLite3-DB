#available data was in csv format
#imported csv file to sqlite3 DB

#imported csv and sqlite3 libraries
import csv
import sqlite3

#created a connection to the "try2" DB and opened a cursor to that connection
conn = sqlite3.connect('try2.sqlite3')
cur = conn.cursor()

#created a table
cur.executescript('''
DROP TABLE IF EXISTS info;

CREATE TABLE info(
    age INTEGER NOT NULL,
    job TEXT NOT NULL,
    marital TEXT NOT NULL,
    education TEXT NOT NULL,
    defaultt TEXT NOT NULL,
    balance INTEGER NOT NULL,
    housing TEXT NOT NULL,
    loan TEXT NOT NULL,
    contact TEXT NOT NULL,
    day INTEGER NOT NULL,
    month TEXT NOT NULL,
    duration INTEGER NOT NULL,
    campaign INTEGER NOT NULL,
    pdays INTEGER NOT NULL,
    previous INTEGER NOT NULL,
    poutcome TEXT NOT NULL,
    y TEXT NOT NULL
)
''')

#opened the .csv file in text reading mode
csvfhandle = open('bank.csv', 'rt', errors='ignore')
csvreader = csv.reader(csvfhandle)

#for loop to read the stream returned by open() above and insert the data into the table
for entry in csvreader:
    cur.execute('INSERT INTO info VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entry)

#closing all the connections
csvfhandle.close()
conn.commit()
conn.close()
