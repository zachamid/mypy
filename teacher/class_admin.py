#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import session,common_components, db_connection

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

if session.in_session():
	cookie.load(string_cookie)
	session.print_cookie()
	if cookie['type'].value == 'Student':
		print 'Location:../index.py'
else:
	print 'Location: index.py'
print """Content-type: text/html\n\n

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../user_functions.js'></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
	</head>
	<body>
		<div class="container">
"""
common_components.print_navbar_teacher(cookie['id'].value, 'site_admin')
print """\n
    		<div class="container col-sm-6 col-md-9">
    			<div class="container" style="width:100%">
    				<div class="panel panel-default translucent">
      					<h3>Classes Managed</h3>
      				</div>
      				<div class="panel panel-default translucent">
      					<table>
      						<tr>
      							<th>ID</th>
      							<th>Name</th>
      							<th>School</th>
      							<th></th>
      						</tr>
"""
sql_query = """ SELECT * FROM Class 
				INNER JOIN TeacherClassRelationship 
				ON Class.ClassID=TeacherClassRelationship.ClassID 
				WHERE TeacherID="""+str(cookie['id'].value);
cursor = db_connection.get_connection()
cursor.execute(sql_query)
class_records = cursor.fetchall()
for record in class_records:
	print '<tr>'
	print '<td>'+record['ClassID']+'</td>'
	print '<td>'+record['ClassName']+'</td>'
	print '<td>'+record['School']+'</td>'
	print '<td>Remove</td>'
	print '</tr>'
print """\n
      					</table>
      					
      				</div>
      				<div class="panel panel-default translucent">
      					<h3>Student Progress</h3>
      				</div>
      				<div class="panel panel-default translucent">
      					<table id="classList">
      						Still in Progress
      					</table>
      				</div>
      			</div>
      		</div>
		</div>
	</body>
</html>
"""