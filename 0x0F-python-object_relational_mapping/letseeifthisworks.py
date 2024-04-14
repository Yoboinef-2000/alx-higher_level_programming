import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="hbtn_0e_0_usa",
    charset="utf8"
)

# Verify the connection
if connection.is_connected():
    print("Connected to MySQL Server")

    # Perform database operations here

    # Close the connection
    connection.close()
    print("Connection closed")