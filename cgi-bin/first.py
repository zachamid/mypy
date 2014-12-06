#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
cgitb.enable()

posted_data = cgi.FieldStorage()
cmd = posted_data['cmd']
db = MySQLdb.connect('localhost','root','S0crat3s34!','test', cursorclass=MySQLdb.cursors.DictCursor);
cursor = db.cursor()
sql_query=''
if cmd != "Schools":
	sql_query = "SELECT DISTINCT School FROM Class"
elif(cmd == 'Classes'):
	param = posted_data['param']
	sql_query = "SELECT * FROM Classes WHERE School='"+param+"'"
elif(cmd == 'Progress'):
	param = posted_data['param']
	sql_query = "SELECT * FROM Progress WHERE StudentID='"+str(param)+"'"
else:
	param = posted_data['param']
	sql_query = "SELECT Email FROM Student WHERE Email='"+param+"' UNION "
	sql_query = sql_query+"SELECT Email FROM Teacher WHERE Email='"+param+"'"

cursor.execute(sql_query)
ver = cursor.fetchall()    
db.close()    
print """content-type: text/html

<html><body>"""
print 'COMMAND'+posted_data['cmd']+"</br>"
print json.dumps(ver)

print "</body></html>"