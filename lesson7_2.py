import sqlite3 as s3

with s3.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS game(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    old INTEGER NOT NULL DEFAULT 0,
    title DEFAULT 0,
    score INTEGER
    )''')
    # cur.execute('''INSERT INTO game (name, old, title, score) VALUES ('beka',12,'',12)''')

    # cur.execute('''UPDATE game SET name="beka" WHERE id=3 or name="q"''')
    cur.execute('''DELETE FROM game WHERE id<9''')



    cur.execute('''SELECT rowid,* FROM game''')
    for row in cur.fetchall():
        print(row)