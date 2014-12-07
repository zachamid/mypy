#!/usr/bin/python

import cgi
import cgitb
import os
#import MySQLdb
#import MySQLdb.cursors
#import db_connection
cgitb.enable()

#db = db_connection.get_connection()
#posted_data = cgi.FieldStorage()

path = '../../tasks/'
files = os.listdir(path)

print """content-type:text/html

<html><body>
"""
for file in files:
	print file+"</br>"

print "</body></html>"