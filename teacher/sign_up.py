#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import session,common_components, sign_up

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

print """\n
    <div class="container"><div class="panel panel-default translucent"><h3>Teacher Sign Up</h3></div><div class="panel panel-default translucent">
      <h4>Teacher Details</h4>"""
sign_up.print_details_form()
print """\n    </div></div>
    <div class="container">
      <input type="button" value="Submit" class="btn btn-default" onclick="sign_up()">
    </div>
    &nbsp
  </body>
</html>		
