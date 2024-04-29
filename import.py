import sqlite3
import csv

#connect to .db
conn = sqlite3.connect('startups.db')
cursor = conn.cursor()
#create table in .db
cursor.execute('''CREATE TABLE IF NOT EXISTS startups (
                    name TEXT,
                    location TEXT,
                    category TEXT,
                    employees INTEGER,
                    raised INTEGER,
                    valuation INTEGER,
                    founded INTEGER,
                    stage TEXT,
                    ceo TEXT,
                    info TEXT
               )''')

#read .csv and insert data to .db
with open('startups-formatted.tsv', 'r') as formatted:
    reader = csv.reader(formatted, delimiter='\t')
    #skip header
    next(reader)
    for row in reader:
        cursor.execute('INSERT INTO startups VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)


#commit transaction and close connection
conn.commit()
conn.close()