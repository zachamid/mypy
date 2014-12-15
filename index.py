#!/usr/bin/env python

import session, Cookie, cgi, cgitb, os, common_components

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

# If new session
if session.in_session():
	cookie.load(string_cookie)
	session.print_cookie()
print """Content-type: text/html\n\n

<html><head>
<script src="/jquery-1.11.1.min.js"></script>
<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
<script src='user_functions.js'></script>
<link rel="stylesheet" type="text/css" href="general_style.css">
</head><body>"""
if not session.in_session():
	common_components.print_header()
else:
	if cookie['type'].value == 'Student':
		common_components.print_navbar(cookie['id'].value,'')
	else:
		common_components.print_navbar_teacher(cookie['id'].value,'')

print """\n
 <div class="col-xs-12 col-md-6 col-sm-12 ">
    	<div class="panel panel-default translucent"><div class="panel-body">
    		<h3><a href="sign_up.php">STUDENTS: Sign Up for MyPy</a></h3>
    		<h4><ul>
    			<li>Learning in Python, one of the simplest and most intuitive languages in industry.</li>
    			<li>Each concept is modularised into a exercises, so as to avoid confusion</li>
    			<li>Follows the AQA Computer Science Syllabus, while also taking into consideration, Prof. Steve Furber's paper 'Shut Down or Restart?' </li>
       		</ul></h4>
    	</div></div>
    </div>
    <div class="col-xs-12 col-md-6 col-sm-12">
    	<div class="panel panel-default translucent"><div class="panel-body">
    		<h3><a href="/teacher/index.php">TEACHERS: Sign Up for MyPy</a></h3>
    		<h4>Keep a track of how well your students are doing by signing in or signing up as a teacher</h4>
    	</div></div>
    </div>
    </div>
  	</body>
</html>
"""