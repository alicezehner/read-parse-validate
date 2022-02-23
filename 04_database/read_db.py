import mysql.connector

# log in to database
cnx = mysql.connector.connect(user='root',
    password='password',
    host='127.0.0.1',
    database='sys',
    auth_plugin='mysql_native_password')

cursor = cnx.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)

#loop through data
for row in cursor.fetchall():
    print(row)

#clean up
cursor.close()
cnx.close()