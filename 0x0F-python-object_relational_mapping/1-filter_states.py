#!/usr/bin/python3

"""Import the sys and MySQLdb modules."""
import sys
import MySQLdb

if __name__ == "__main__":

    theUsername = sys.argv[1]
    thePassword = sys.argv[2]
    theDatabase = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=theUsername,
                           passwd=thePassword, db=theDatabase)
    dbcur = db.cursor()
    nameStart = "N%"
    dbcur.execute("""SELECT * FROM states WHERE BINARY name
                  LIKE %s ORDER BY id""", (nameStart, ))
    everything = dbcur.fetchall()
    for stts in everything:
        print(stts)

    dbcur.close()
    db.close()
