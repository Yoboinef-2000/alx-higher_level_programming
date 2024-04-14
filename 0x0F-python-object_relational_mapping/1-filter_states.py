#!/usr/bin/python3
"""lists all the states that are like a given name from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    match = "N%"
    cur.execute("""SELECT * FROM states WHERE BINARY name
                LIKE %s ORDER BY id""", (match, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    