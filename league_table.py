#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
from operator import itemgetter, attrgetter
from  task_correction import calc_score as calc_score
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	if cookies['type'].value == 'Teacher':
		print 'Location: index.py'
else:
	print 'Location: index.py'

cursor = db_connection.get_connection()
cursor.execute('''SELECT FirstName, LastName, ClassID FROM Student WHERE StudentID=%s''' % (cookies['id'].value))
student_record = cursor.fetchone()
cursor.execute('''SELECT StudentID, FirstName, LastName FROM Student
					WHERE ClassID=%s''' % (student_record['ClassID']))
class_list = cursor.fetchall()
league_entry = []
for student in class_list:
	new_entry = {}
	new_entry['student'] = str(student['StudentID'])
	new_entry['score'] = 0
	cursor.execute('''SELECT Correctness_Points,Similarity_Points, Attempts_Points, Time_Points 
						FROM Progress WHERE StudentID='''+str(student['StudentID']))
	progress_records = cursor.fetchall()
	for record in progress_records:
		score = calc_score(record['Correctness_Points'],record['Similarity_Points'],record['Attempts_Points'],record['Time_Points'])
		new_entry['score'] += score
	new_entry['no_tasks'] = len(progress_records)
	new_entry['name']= student['FirstName']+' '+student['LastName']
	league_entry.append(new_entry)
		
league_order=sorted(league_entry, key=lambda e: e['score'])

print """Content-type: text/html\n\n


"""
print """\n
<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    """
common_components.print_navbar(cookies['id'].value,'')
print """\n
		<div class="container col-sm-6 col-md-9">
			<div class="panel  panel-default translucent">
				<table width="100%">
				<tr>
					<td><b>ID</b></td>
					<td><b>Name</b></td>
					<td><b>Tasks Attempted</b></td>
					<td><b>Score</b></td>
				</tr>"""
for id in league_order:
	print '<tr>'
	if id['student'] == cookies['id'].value:
		print '<td><b>%s</b></td><td><b>%s</b></td><td><b>%s</b></td><td><b>%s</b></td>' % (str(id), str(league_entry[id]['name']),str(league_entry[id]['no_tasks']),str(league_entry[id]['score']))
	else:
		print '<td>%s</td><td>%s</td><td>%s</td><td>%s</td>' % (str(id[student]), str(id['name']),str(id['no_tasks']),str(id['score']))

	print '</tr>'
print '</table></div></div></body></html>'