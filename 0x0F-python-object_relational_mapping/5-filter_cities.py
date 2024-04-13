#!/usr/bin/python3

"""Import the sys and MySQLdb modules."""
import sys
import MySQLdb

if __name__ == '__main__':

    theUsername = sys.argv[1]
    thePassword = sys.argv[2]
    theDatabase = sys.argv[3]
    theUserInput = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=theUsername, passwd=thePassword,
                         db=theDatabase, charset="utf8")
    dbcur = db.cursor()
    dbcur.execute("""SELECT cities.name
                FROM cities LEFT JOIN states
                  ON states.id = cities.state_id
                  WHERE states.name = %s
                  ORDER BY cities.id ASC""", (theUserInput, ))

    everything = dbcur.fetchall()
    theformattedArray = []
    for stts in everything:
        theformattedArray.append(stts[0])

    print(", ".join(theformattedArray))
    dbcur.close()
    db.close()
