#!/usr/bin/python3

"""Import the sys and MySQLdb modules."""
import sys
import MySQLdb

if __name__ == '__main__':

    theUsername = sys.argv[1]
    thePassword = sys.argv[2]
    theDatabase = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=theUsername, passwd=thePassword,
                         db=theDatabase, charset="utf8")
    dbcur = db.cursor()
    dbcur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities LEFT JOIN states
                  ON states.id = cities.state_id
                  ORDER BY cities.id ASC;""")

    everything = dbcur.fetchall()
    for stts in everything:
        print(stts)

    dbcur.close()
    db.close()
