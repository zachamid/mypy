#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
values_to_change = list();
if 'FirstName' in posted_data:
	values_to_change.append('FirstName="'+posted_data['FirstName'].value+'"')
if 'LastName' in posted_data:
	values_to_change.append('LastName="'+posted_data['LastName'].value+'"')
if 'Password' in posted_data:
	values_to_change.append('Password="'+posted_data['Password'].value+'"')

values_to_change =  ",".join(values_to_change);

cursor = db_connection.get_connection()

id = posted_data['id'].value
type = posted_data['type'].value
print """content-type:text/html

"""


sql_statement = 'UPDATE '+type+' SET '+values_to_change+' WHERE '+type+'ID='+id
cursor.execute(sql_statement)
print cursor.rowcount