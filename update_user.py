#!/usr/bin/python

import cgi
import cgitb
import MySQLdb
import MySQLdb.cursors
import db_connection
import session
cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()
cookie.load(string_cookie)
session.print_session()
print """content-type:text/html

"""
db = db_connection.get_connection()
posted_data = cgi.FieldStorage()
id = cookie['id'].value
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