"""An example of using Python to read data from a MySQL
database table. See: https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html """
import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='dogs')

cursor = cnx.cursor()

query = "select id as dogid, name, age from dog"


cursor.execute(query)

for (dogid, name, age) in cursor:
    print("{} - {} is {:5d}".format(dogid, name, age))

cursor.close()
cnx.close()
