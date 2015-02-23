#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection, hashlib
cgitb.enable()

posted_data = cgi.FieldStorage()
table = posted_data['Table'].value
cursor = db_connection.get_connection()
password = hashlib.sha256(posted_data['Password'].value).hexdigest()
email = posted_data['Email'].value
fName = posted_data['FirstName'].value
lName = posted_data['LastName'].value
sql_query = '''INSERT INTO %s (FirstName, LastName, Email, Password) 
				VALUES (%s,%s,%s,%s)''' % (table,fName,lName,email,password)
#cursor.execute(sql_query)
#id = cursor.lastrowid

print """Content-type: text/html\n\n


"""
#print id
print sql_query
