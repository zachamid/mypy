#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
values_to_change = list();
for key in posted_data:
	if key != 'id' and key != 'type':
		values_to_change.append(key.'="'+posted_data[key].value+'"')

values_to_change =  ",".join(values_to_change);

cursor = db_connection.get_connection()

id = posted_data['id'].value
type = posted_data['type'].value
print """content-type:text/html

"""


sql_statement = 'UPDATE '+type+' SET '+values_to_change+' WHERE '+type+'ID='+id
cursor.execute(sql_statement)
print cursor.rowcount