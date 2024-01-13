#!/usr/bin/python3
'''
Script that takes in an argument and displays all values
in th states table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cur = db.cursor()
    name = sys.argv[4]

    # format to create the SQL query with the user input
    q = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(name)
    numrows = cur.execute(q)
    rows = cur.fetchall()
    for row in rows:
        index, state = row
        print("({}, '{}')").format(index, state)
    cur.close()
    db.close()
