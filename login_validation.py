#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
import hashlib
cgitb.enable()

posted_data = cgi.FieldStorage()
email = posted_data['email'].value
password = posted_data['password'].value
type_of_user = posted_data['type'].value
cursor = db_connection.get_connection()
sql = "SELECT * FROM "+type_of_user+" WHERE Email='"+email+"'"
cursor.execute(sql)
result = cursor.fetchall()

print """content-type: text/html

"""
if len(result) != 0:
	if result[0]['Password'] == hashlib.sha256(password).hexdigest():
		id = result[0][type_of_user+'ID']
		print id
	else:
		print -1
else:
	print -1
