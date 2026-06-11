import sqlite3
import sys

db = 'db.sqlite3'
conn = sqlite3.connect(db)
cur = conn.cursor()
print('Connected to', db)
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = cur.fetchall()
print('tables:', tables)
try:
    cur.execute("SELECT app, name FROM django_migrations WHERE app='base' ORDER BY id")
    rows = cur.fetchall()
    print('base migrations:', rows)
except Exception as e:
    print('Could not read django_migrations:', e)

cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
for name, sql in cur.fetchall():
    if 'aarthik_barsa' in name or (sql and 'aarthik_barsa' in sql):
        print('Found aarthik_barsa in table:', name)
        print(sql)

conn.close()
