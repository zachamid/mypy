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
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
		<script>
			function open_correction(taskID){
				var mapForm = document.createElement("form");
	    		mapForm.method = "POST";
	  		  	mapForm.action = "/correction_page.py";
				var taskid = document.createElement("input");
			    taskid.type = "text";
			    taskid.name = "task_id";
				taskid.value = taskID;
			    mapForm.appendChild(taskid);
    			document.getElementById('postform').appendChild(mapForm);
    			mapForm.submit();
			}
		</script>
		<style>
			table,td,th, tr {
    			border: 0.5px solid black;
    			padding: 10px;
			}
		</style>
	</head>
	<body>"""
common_components.print_navbar(cookies['id'].value,'')
print """\n
		<div class="container col-sm-6 col-md-9">
			<div class="panel  panel-default translucent">
				<table width="100%">
				<tr>
					<td><b>ID</b></td>
					<td><b>Task Name</b></td>
					<td><b>Date Started</b></td>
					<td><b>Date Modified</b></td>
					<td><b>Date Completed</b></td>
					<td><b>Score</b></td>
				</tr>"""
for record in progress_records:
	print '<tr onclick=\'open_correction('+str(record['TaskID'])+')\'><td>'+str(record['TaskID'])+'</td>'
	print '<td>'+record['Title']+'</td>'
	print '<td>'+record['DateStarted'].strftime("%Y-%m-%d %H:%M:%S")+'</td>'
	if record['DateModified'] is not None:
		print '<td>'+record['DateModified'].strftime("%Y-%m-%d %H:%M:%S")+'</td>'
	else:
		print '<td></td>'
	if record['DateCompleted'] is not None:
		print '<td>'+record['DateCompleted'].strftime("%Y-%m-%d %H:%M:%S")+'</td>'
		score = (float)((40*record['Correctness_Points'])+(30*record['Similarity_Points'])+(15*record['Time_Points'])+(15+record['Attempts_Points']))
		print '<td>'+str(score)+'</td>'
	else:
		print '<td></td>'
		print '<td></td>'
	print '</tr>'
print """\n	</table>
		</div></div>
		<div id="postform" style="display: none;"></div>
	</body>
</html>
"""