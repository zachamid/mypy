#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import session,common_components

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
    	<script type="text/javascript">
      
    	</script>
  	</head>
  	<body>
  		<div class="container">
"""
common_components.print_navbar_teacher(cookie['id'].value,'user_page')
cursor = db_connection.get_connection()
sql_query = 'SELECT * FROM Teacher WHERE TeacherID='+cookie['id'].value
cursor.execute(sql_query)
record = cursor.fetchone()
print """\n
    		<div class="container">
      		<h3>Personal Details</h3>
      		<div class="panel panel-default">
        		<table width="100%" style="border-spacing:10px">
          			<tr>
            			<td style="width:50%">
              				First Name: <input class="form-control" type="text" id="FirstName" value="""+record['FirstName']+""">
            			</td>
            			<td>
              				<div id="FirstName_alert"></div>
            			</td>
          			</tr>
          			<tr>
            			<td style="width:50%">
              				Last Name: <input class="form-control" type="text" id="LastName" value="""+record['LastName']+""">
            			</td>
            			<td>
              				<div id="LastName_alert"></div>
            			</td>
          			</tr>
          			<tr>
            			<td style="width:50%">
              				Email: <input class="form-control" type="text" id="Email" value="""+record['Email']+""">
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
            				<input class="form-control" type="password" name="confirm_New_Password" placeholder="Confirm New Password">
            			</td>
            			<td>
               				<div id="confirm_New_Password_alert"></div>
            			</td>
          			</tr>
          			<tr><td>
         				<button class="form-control" onclick='update_user('Teacher',"""+record['TeacherID']+""")' type="button">
									Update
						</button>
          			<td></tr>
        		</table>
      		</div>
    	</div>
    	</div>
  </body>
</html>
"""