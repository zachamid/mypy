#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()
cookie.load(string_cookie)
session.print_cookie()

db = db_connection.get_connection()
posted_data = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST'})
id = cookie['id'].value
type = cookie['type'].value
print """content-type:text/html

"""
values_to_change = list();
if 'FirstName' in posted_data:
	values_to_change.append('FirstName="'+posted_data['FirstName'].value+'"')
if 'LastName' in posted_data:
	values_to_change.append('LastName="'+posted_data['LastName'].value+'"')
if 'Password' in posted_data:
	values_to_change.append('Password="'+posted_data['Password'].value+'"')

values_to_change =  ",".join(values_to_change);

sql_statement = 'UPDATE '+type+' SET '+values_to_change+' WHERE '+type+'ID='+id
print sql_statement
#cursor = db.cursor()
#cursor.execute(sql_statement)
#print cursor.rowcount