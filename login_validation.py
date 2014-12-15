#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
import db_connection,session
cgitb.enable()

print """content-type: text/html

<html><body>"""
posted_data = cgi.FieldStorage()
if 'email' in posted_data and 'password' in posted_data:
	email = posted_data['email'].value
	password = posted_data['password'].value
	type_of_user = posted_data['type'].value
	db = db_connection.get_connection()
	sql = "SELECT * FROM "+type_of_user+" WHERE Email='"+email+"'"
	cursor = db.cursor()
	cursor.execute(sql)
	result = cursor.fetchall()
	if len(result) != 0:
		if result[0]['Password'] == password:
			print result[0][type_of_user+'ID']
		else:
			print -3
	else:
		print -2
else:
	print -1

print "</body></html>"