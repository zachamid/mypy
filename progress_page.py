#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	if cookies['type'].value == 'Teacher':
		print 'Location: index.py'
else:
	print 'Location: index.py'

cursor = db_connection.get_connection()
cursor.execute('''SELECT * FROM Progress
					INNER JOIN Task
					ON Progress.TaskID = Task.TaskID
					WHERE Progress.StudentID=%s''',(cookies['id'].value))
progress_records = cursor.fetchall()

print """Content-type: text/html\n\n

<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="jquery-linedtextarea.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
	</head>
	<body>"""
common_components.print_navbar(cookies['id'].value,'')
print """\n
		<div class="container col-sm-6 col-md-9">
			<div class="panel  panel-default translucent">
			<table>
				<tr>
					<td>ID</td>
					<td>Task Name</td>
					<td>Date Started</td>
					<td>Date Modified</td>
					<td>Date Completed</td>
					<td>Points</td>
				</tr>"""
for record in progress_records:
	print '<tr><td>'+str(record['TaskID'])+'</td>'
	print '<td>'+record['Title']+'</td>'
	print '<td>'+record['DateStarted'].strftime("%Y-%m-%d %H:%M:%S")+'</td>'
	print '<td>'+record['DateModified'].strftime("%Y-%m-%d %H:%M:%S")+'</td>'
	print '<td>'+record['DateCompleted'].strftime("%Y-%m-%d %H:%M:%S")+'</td>'
	print '<td>'+str(record['Points'])+'</td></td>'
print """\n	</table>
		</div></div>
	</body>
</html>
"""