#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
table = posted_data['table'].value
columns = posted_data['columns'].value
values = posted_data['values'].value
sql_query = "INSERT INTO %s(%s) VALUES(%s)",(table,columns,values)
db = db_connection.get_connection()
cursor = db.cursor()
cursor.execute(sql_query)
id = cursor.lastrowid

print """content-type:text/html

"""
print id