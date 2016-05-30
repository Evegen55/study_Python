'''
Created on 30.05.2016 г.

@author: Lartsev
'''
import sqlite3

conn = sqlite3.connect('emaildb_task.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open('mbox.txt')

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    dom_splt = email.split('@')
    dom_name = dom_splt[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (dom_name,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (dom_name,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (dom_name,))
    conn.commit()