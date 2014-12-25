#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
table = posted_data['table'].value
columns = posted_data['columns'].value
values = posted_data['values'].value
sql_query = "INSERT INTO "+table+"("+columns+") VALUES("+values+")"
cursor = db_connection.get_connection()
cursor.execute(sql_query)
id = cursor.lastrowid

print """content-type:text/html

"""
print sql_query
print id