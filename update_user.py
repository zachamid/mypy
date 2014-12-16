#!/usr/bin/python

import cgi,cgitb,MySQLdb,MySQLdb.cursors,db_connection,session,os
cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()
cookie.load(string_cookie)
session.print_cookie()

db = db_connection.get_connection()
posted_data = cgi.FieldStorage()
id = cookie['id'].value
type = cookie['type'].value
print """content-type:text/html

"""
type = posted_data['type'].value
values_to_change = list();
if 'FirstName' in posted_data:
	values_to_change.append('FirstName="'+posted_data['FirstName']+'"')
if 'LastName' in posted_data:
	values_to_change.append('LastName="'+posted_data['LastName']+'"')
if 'Password' in posted_data:
	values_to_change.append('Password="'+posted_data['Password']+'"')

values_to_change =  ",".join(values_to_change);

sql_statement = 'UPDATE '+type+' SET '+values_to_change+' WHERE '+type+'ID='+id
