#!/usr/bin/python3
'''
Script that lists all stats with a name starting with N from db hbtn_0e_0_usa
'''

import MySQLdb
import sys

db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
)
cur = db.cursor()
numrows = cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    index, state = row
    if state[0] == 'N':
        print("({}, '{}')".format(index, state))
cur.close()
db.close()
