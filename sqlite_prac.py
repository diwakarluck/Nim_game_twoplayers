import sqlite3

conn = sqlite3.connect('blog.db')

conn.execute('''CREATE TABLE IF NOT EXISTS CONTACT
             (id int primary key,
             name text not null,
             phone_num text not null,
             mes char(100),
             email text not null);''')

conn.execute('''CREATE TABLE IF NOT EXISTS POSTES
            (title TEXT primary key,
            sub_title TEXT,
            byname TEXT,
            content CHAR(100),
            slug CHAR(40));''')

conn.execute('''INSERT INTO POSTES (TITLE, SUB_TITLE, BYNAME, CONTENT, SLUG)
            VALUES ('Python post', 'Python Based Flask framework','Diwakar Ranjan', 'This is my first project on python based flask framework', 'python-first');''')
conn.execute('COMMIT;')

cursor = conn.execute("select * from POSTES")
for i in cursor:
    print(i)

