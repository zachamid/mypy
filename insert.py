#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, MySQLdb.cursors, db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
table = posted_data['table'].value
columns = posted_data['columns'].value
values = posted_data['values'].value
cursor = db_connection.get_connection()
sql_query =''
if table == 'TeacherClassRelationship':
	classID, teacherID = values.split(',');
	sql_query = '''SELECT * FROM TeacherClassRelationship
					WHERE ClassID='''+ classID+' AND TeacherID='+teacherID
	cursor.execute(sql_query)
	if cursor.rowcount != 0:
		id = 0
if(id):
	sql_query = '''INSERT INTO %s(%s) VALUES(%s)''' % (table, columns, values)
	cursor.execute(sql_query)
	id = cursor.lastrowid

print """content-type:text/html

"""
print sql_query
print id
