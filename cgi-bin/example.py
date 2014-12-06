#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
cgitb.enable()

db = MySQLdb.connect('localhost','root','S0crat3s34!','test', cursorclass=MySQLdb.cursors.DictCursor);
cursor = db.cursor()
cursor.execute("SELECT * FROM Student")
ver = cursor.fetchall()    
db.close()    
print """content-type: text/html

<html><body>"""
for line in ver:
    print json.dumps(line)

print "</body></html>"