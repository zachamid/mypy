#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
email = posted_data['email'].value
password = posted_data['password'].value
type_of_user = posted_data['type'].value
db = db_connection.get_connection()
sql = "SELECT * FROM "+type_of_user+" WHERE Email='"+email+"'"
cursor = db.cursor()
cursor.execute(sql)
result = cursor.fetchAll()

print """content-type: text/html

<html><body>"""
 
 if result[0]['Password'] == password:
 	echo 1
 else:
 	echo 0
 
 print "</body></html>"