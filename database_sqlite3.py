import sqlite3

conn = sqlite3.connect('site.db')

conn.execute('''CREATE TABLE IF NOT EXISTS POST
            (TITLE TEXT,
            SUB_TITLE TEXT,
            CONTENT CHAR(100));''')

conn.execute('''INSERT INTO POST (TITLE, SUB_TITLE, CONTENT)
            VALUES ('Python post', 'Python Based Flask framework', 'This is my first project on python based flask framework');''')
conn.execute('COMMIT;')

cursor = conn.execute("select * from POST")
for i in cursor:
    print(i)