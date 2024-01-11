#!/usr/bin/python3
''' Script that lists all stats from datatbase hbtn_0e_0_usa '''

import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='Password123#@!', db='hbtn_0e_0_usa')
cur = db.cursor()
numrows = cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    index, state = row
    print("({}, '{}')".format(index, state))
