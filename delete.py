#!/usr/bin/python

import cgi, cgitb, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
table = posted_data['table'].value
id = posted_data['id'].value
sql_query = "DELETE FROM "+table+" WHERE "+table+"ID="+id
print sql_query
cursor = db_connection.get_connection()
cursor.execute(sql_query)