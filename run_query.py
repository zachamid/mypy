#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
cmd = posted_data['cmd'].value
db = db_connection.get_connection()
cursor = db.cursor()
sql_query=''
if cmd == "Schools":
	sql_query = "SELECT DISTINCT School FROM Class"
elif(cmd == 'Classes'):
	param = posted_data['param'].value
	sql_query = "SELECT * FROM Class WHERE School='"+param+"'"
elif(cmd == 'Progress'):
	param = posted_data['param'].value
	sql_query = "SELECT * FROM Progress WHERE StudentID='"+str(param)+"'"
elif(cmd == 'CheckEmail'):
	param = posted_data['param']
	sql_query = "SELECT Email FROM Student WHERE Email='"+param+"' UNION "
	sql_query = sql_query+"SELECT Email FROM Teacher WHERE Email='"+param+"'"
elif(cmd == 'ClassList'):
	param = posted_data['param'].value
	sql_query = "SELECT * FROM Student WHERE ClassID="+param

cursor.execute(sql_query)
db.close()    
print """content-type: text/html

<html><body>"""
print json.dumps(ver)

print "</body></html>"