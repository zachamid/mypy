#!/usr/bin/python

import cgi
import cgitb
#import MySQLdb
#import MySQLdb.cursors
#import db_connection
cgitb.enable()

#db = db_connection.get_connection()
#posted_data = cgi.FieldStorage()
#
##################CODE ABOVE THIS LINE WILL SORT OUT COOKIES AND POSTED DATA#####
id='1'
posted_data = {'type':'Student','FirstName':'Zac', 'LastName':'Hamid','Password':'Password'}
type = posted_data['type']
values_to_change = list();
if 'FirstName' in posted_data:
	values_to_change.append('FirstName="'+posted_data['FirstName']+'"')
if 'LastName' in posted_data:
	values_to_change.append('LastName="'+posted_data['LastName']+'"')
if 'Password' in posted_data:
	values_to_change.append('Password="'+posted_data['Password']+'"')

values_to_change =  ",".join(values_to_change);
print """content-type:text/html

<html><body>"""
print 'UPDATE '+type+' SET '+values_to_change+' WHERE '+type+'ID='+id
print "</body></html>"