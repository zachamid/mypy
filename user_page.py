#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,session, common_components
cgitb.enable()

print "Content-type: text/html"
cookie = session.return_cookie()
if not session.in_session():
	print """Location:index.py

"""
else:
	print """

"""
print """\n
<html>
  	<head>
    	<script src="jquery-1.11.1.min.js"></script>
    	<script src="user_functions.js"></script>
    	<title>Welcome</title>
    	<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="general_style.css" rel="stylesheet">
    </head>
  	<body>
    	<div class="container">"""
common_components(cookie['id'].value, 'user_page')
db = db_connection.get_connection()
cursor = db.cursor()
sql = 'SELECT * FROM Student INNER JOIN Class ON Student.ClassID=Class.ClassID WHERE StudentID='+cookie['id'].value
cursor.execute(sql)
person_record = cursor.fetchone()
print """\n
    	<div class="container col-sm-6 col-md-9">
    		<div class="container" style="width:100%">
    			
      			<div class="panel panel-default translucent">
      			<h3>Personal Details</h3></div>
      			<div class="panel panel-default translucent">
        			<table width="100%" style="border-spacing:10px">
          				<tr>
            				<td style="width:50%">
              					First Name: <input class="form-control" type="text" id="FirstName" value="%s">
            				</td>
            				<td>
              					<div id="FirstName_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					Last Name: <input class="form-control" type="text" id="LastName" value="%s" >
            				</td>
            				<td>
              					<div id="LastName_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					Email: <input class="form-control" type="text" id="Email" value="%s" readonly>
            				</td>
            				<td>
              					<div id="Email_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					<input class="form-control" type="password" id="Password" placeholder="Old Password">
            				</td>
            				<td>
               					<div id="Password_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					<input class="form-control" type="password" id="new_Password" placeholder="New Password">
            				</td>
            				<td>
               					<div id="new_Password_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					<input class="form-control" type="password" id="confirm_New_Password" placeholder="Confirm New Password">
            				</td>
            				<td>
               					<div id="confirm_New_Password_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
               					<div id="class_place">%s</div>
            				</td>
            				<td>
            					<button class="form-control" onclick='update_user("Student", %d)' type="button">
									Update
								</button>
            				</td>
          				</tr>
        			</table>
      			</div>
    		</div>
""" % person_record['FirstName'], person_record['LastName'], person_record['Email'], person_record['ClassName'], person_record['StudentID']
print """\n    		
    		<div class="container" style="width:100%">
      			<div class="panel panel-default translucent"><h3>Tasks</h3></div>
      			<div class="panel panel-default translucent">
        			<table id="task_list" width="100%" style="border-spacing:10px">
          				<tr><th>ID</th>
           					<th>Task</th>
           					<th>Date Started</th>
           					<th>Last Opened</th>
           					<th>Date Completed</th></tr>
"""
sql_query = 'SELECT * FROM Progress INNER JOIN Task ON Progress.TaskID=Task.TaskID WHERE Progress.StudentID='+person_record['StudentID'];
cursor.execute(sql_query)
progress_records = cursor.fetchall()
for record in progress_records:
  	print """\n<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
  		""" % record['TaskID'],record['TaskName'],record['DateStarted'],record['DateModified'],record['DateCompleted']
print """\n</table>
      			</div>
    		</div>
    	</div></div>
  	</body>
</html>"""