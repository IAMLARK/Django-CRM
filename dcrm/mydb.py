import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Mwangi2024',
) 

cursorobject = dataBase.cursor()

cursorobject.execute("CREATE DATABASE elderco")

print("All done")
