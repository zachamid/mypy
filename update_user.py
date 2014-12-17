#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection, os
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

db = db_connection.get_connection()


string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()
cookie.load(string_cookie)
id = cookie['id'].value
type = cookie['type'].value
print """content-type:text/html

"""


sql_statement = 'UPDATE '+' SET '+values_to_change+' WHERE '+'ID='
print sql_statement
print posted_data
#cursor = db.cursor()
#cursor.execute(sql_statement)
#print cursor.rowcount