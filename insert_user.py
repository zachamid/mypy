#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection, hashlib
cgitb.enable()

posted_data = cgi.FieldStorage()
table = posted_data['table'].value
cursor = db_connection.get_connection()
password = hashlib.sha256(posted_data['Password'])
