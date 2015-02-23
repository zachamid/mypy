#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
cgitb.enable()
	    
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	print 'Location: user_page.py'
print "Content-type: text/html"

print """\n


<html>
	<head>
  		<script src="jquery-1.11.1.min.js"></script>
  		<script src='user_functions.js'></script>
  		<title>Sign Up to MyPy</title>
  		<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  		<link rel="stylesheet" type="text/css" href="general_style.css">
  		<script>
			function sign_up(){
  				var fields = ['FirstName', 'LastName', 'Email','Password','confirm_Password'];
    			var flag = 0;
    			for(counter =0; counter < fields.length; counter++){
    				var out = validate_detail(fields[counter]);
      				if(out == 1){
        				flag = 1;
      				}
    			}
    			if(flag == 1){
      				alert('Please fix your form and Retry');
    			}
    			else{
    				var student = {};
    				for(counter=0; counter<fields.length-1;counter++){
    					student[fields[counter]]=document.getElementById(fields[counter]).value;
    				}
    				student['ClassID'] = document.getElementById('classes').options[document.getElementById('classes').selectedIndex].value;
					insert_user('Student',student);
    			}
  			}
  		</script>
  	</head>
  	<body>"""
common_components.print_header()
    
print """\n
    	<div class="container"><div class="panel panel-default translucent"><h3>Student Sign Up</h3></br></br>
    		<h4>Student Details</h4>"""
print """\n <table width="100%" style="border-spacing:10px">
        		<tr>
          			<td style="width:50%">
             			<input class="form-control" type="text" id="FirstName" placeholder="First Name" onblur='validate_detail(this.id)'>
          			</td>
          			<td>
           			  	<div id="FirstName_alert"></div>
          			</td>
        		</tr>
        		<tr>
          			<td style="width:50%">
            			<input class="form-control" type="text" id="LastName" placeholder="Last Name" onblur='validate_detail(this.id)'>
          			</td>
          			<td>
            	 		<div id="LastName_alert"></div>
          			</td>
        		</tr>
        		<tr>
          			<td style="width:50%">
            			<input class="form-control" type="text" id="Email" placeholder="Email Address" onblur='validate_detail(this.id)'>
          			</td>
          			<td>
            	 		<div id="Email_alert"></div>
          			</td>
        		</tr>
        		<tr>
          			<td style="width:50%">
            			<input class="form-control" type="password" id="Password" placeholder="Password" onblur='validate_detail(this.id)'>
          			</td>
          			<td>
             			<div id="Password_alert"></div>
          			</td>
        		</tr>
        		<tr>
          			<td style="width:50%">
            			<input class="form-control" type="password" id="confirm_Password" placeholder="Confirm Password" onblur='validate_detail(this.id)'>
          			</td>
          			<td>
             			<div id="confirm_Password_alert"></div>
          			</td>
        		</tr>
      		</table>"""
print """\n    	</div></div>
    	<div class="container"><div class="panel panel-default translucent">
      		<h4>Class Details</h4></br>
      		<table width="100%">
        		<tr><td style="width:50%">
          			<select class="form-control" id="classes" onfocus="getClasses()">"""
sql = '''SELECT ClassID, ClassName FROM Class'''
cursor = db_connection.get_connection()
cursor.execute(sql)
classes = cursor.fetchall()
for single_class in classes:
	print '<option value=\'%s\'>%s</option' % (str(single_class['ClassID']),str(str(single_class['ClassName'])))

print """/n
		</select>
        		</td><td>&nbsp</td></tr>
        		<td>&nbsp</td></tr>
      		</table>
    	</div></div>
    	<div class="container">
      		<input type="button" value="Submit" class="btn btn-default" onclick="sign_up()">
    	</div>&nbsp
  	</body>
</html>	"""
