#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components, db_connection
from task_correction import calc_score as calc_score

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	if cookies['type'].value == 'Student':
		print 'Location:../index.py'
else:
	print 'Location: index.py'

cursor = db_connection.get_connection()

print """Content-type: text/html\n\n



<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../user_functions.js'></script>
    	<title>Class Administration</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		function print_res(taskID,studentID){
	    		data = {taskID:taskID, studentID:studentID}
	    		$.ajax({
      				data : data,
      				url : '/teacher/attempt_info.py',
      				type : "POST",
      				dataType : "html"}).done(function(result){
      					document.getElementById('Attempt').innerHTML = result;
      				});
      			}
    	</script>
	</head>
	<body>
"""
common_components.print_navbar_teacher(cookies['id'].value, 'site_admin')
print """\n
    		<div class="container col-sm-6 col-md-9">
    			<div class="panel panel-default translucent">
"""
sql = '''SELECT TaskID from Task'''
cursor.execute(sql)
tasks = cursor.fetchall()

sql = '''SELECT Student.StudentID, Student.FirstName, Student.LastName FROM Student
		INNER JOIN TeacherClassRelationship
		ON Student.ClassID = TeacherClassRelationship.ClassID
		INNER JOIN Teacher
		ON Teacher.TeacherID = TeacherClassRelationship.ClassID
		WHERE TeacherClassRelationship.TeacherID=%s''' % (str(cookies['id'].value ))
cursor.execute(sql)
student_info = cursor.fetchall()

print '<table><tr><th>Name</th>'
for task in tasks:
	print '<th>%s</th>' % (str(task['TaskID']))
print '</tr>'
for student in student_info:
	print '<tr><td>%s</td>' % (student['FirstName']+' '+student['LastName'])
	for task in tasks:
		print '<td>'
		sql = '''SELECT ProgressID, Correctness_Points, Similarity_Points,
					Attempts_Points, Time_Points
				FROM Progress WHERE StudentID=%d AND TaskID=%d''' % (student['StudentID'], task['TaskID'])
		cursor.execute(sql)
		if cursor.rowcount != 0:
			points = cursor.fetchone()
			print '<a onclick=\'print_rest(%d,%d)\'>' % (student['StudentID'], task['TaskID'])
			print format(calc_score(points['Correctness_Points'],points['Similarity_Points'],points['Attempts_Points'],points['Time_Points']), '.1f')
			print '</a>'
		print '</td>'
	print '</tr>'
print '''\n</table>
			</div>
		</div>
		</br>
		<div class="container col-sm-6 col-md-9">
    		<div id = 'Attempt' class="panel panel-default translucent">
    		</div>
    	</div>
	</body>
</html>'''