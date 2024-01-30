import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql@root'
)

# Prepare cursor object
cursorObject = dataBase.cursor()

#Create the database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")