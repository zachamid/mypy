#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
else:
	print 'Location:index.py'
print """Content-type: text/html\n\n

<html>
  	<head>
    	<script src="jquery-1.11.1.min.js"></script>
    	<script src="user_functions.js"></script>
    	<title>Welcome</title>
    	<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="general_style.css" rel="stylesheet">
    </head>
  	<body>"""
common_components.print_navbar(cookies['id'].value, 'user_page')
cursor = db_connection.get_connection()
sql = '''SELECT * FROM Student 
		INNER JOIN Class 
		ON Student.ClassID=Class.ClassID
		WHERE StudentID='''+cookies['id'].value
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
              					First Name: <input class="form-control" type="text" id="FirstName" value="""+person_record['FirstName']+""">
            				</td>
            				<td>
              					<div id="FirstName_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					Last Name: <input class="form-control" type="text" id="LastName" value="""+person_record['LastName']+""">
            				</td>
            				<td>
              					<div id="LastName_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					Email: <input class="form-control" type="text" id="Email" value="""+person_record['Email']+""" readonly>
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
               					<div id="class_place">"""+person_record['ClassName']+"""\n</div>
            				</td>
            				<td>
            					<button class="form-control" onclick='update_user("Student", """+str(person_record['StudentID'])+""")' type="button">
									Update
								</button>
            				</td>
          				</tr>
        			</table>
      			</div>
    		</div>
"""
rint """\n
    	</div>
  	</body>
</html>"""