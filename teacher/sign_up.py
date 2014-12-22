#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	if cookies['type'].value == 'Student':
		print 'Location:../index.py'
	else:
		print 'Location:index.py'
print """Content-type: text/html\n\n

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
  		<script src='../user_functions.js'></script>
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
    				var teacher = {};
    				for(counter=0; counter<fields.length-1;counter++){
    					teacher[fields[counter]]=document.getElementById(fields[counter]).value;
    				}
    				insert_user('Teacher',teacher);
    			}
  			}
  		</script>
  		<title>Teacher Portal: Sign Up to MyPy</title>
  		<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  		<link href="../general_style.css" rel="stylesheet">
  		<link href="teacher_style.css" rel="stylesheet">
  </head>
  <body>
"""
common_components.print_header_teacher()
print """\n
    <div class="container col-sm-12 col-md-12">
    	<div class="panel panel-default translucent">
    		<h3>Teacher Sign Up</h3>
    	</div>
    	<div class="panel panel-default translucent">
      		<h4>Teacher Details</h4>"""
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
print """\n    </div></div>
    <div class="container">
      <input type="button" value="Submit" class="btn btn-default" onclick="sign_up()">
    </div>
    &nbsp
  </body>
</html>		
"""