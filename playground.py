#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,session, common_components,os
cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

# If new session
if session.in_session():
	cookie.load(string_cookie)
	session.print_cookie()

print """Content-type: text/html\n\n

<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="jquery-linedtextarea.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		$(function() {
			$(".lined").linedtextarea(
			{selectedLine: 1}
			);
		});

		<link rel="stylesheet" type="text/css" href="jquery-linedtextarea.css">
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
	</head>
	<body>
		<div class="container">"""

if not session.in_session():
	common_components.print_header()
else:
	if cookie['type'].value == "Student":
		common_components.print_navbar(cookie['id'].value,'playground')
	else:
		common_components.print_navbar_teacher(cookie['id'].value,'playground')

print """\n
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Python Source Code</div>
				<div class="panel-body">
					<textarea class="form-control code-holder lined" rows="10" id="code">
for i in range(8):
 print i
					</textarea>
					<button class="form-control" onclick='run_code("code","output","error")' type="button">
						Run
					</button>
				</div>
			</div>
		</div>
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Output</div>
				<div class="panel-body">
					<textarea class="form-control code-holder lined" rows="5" id="output"></textarea>
				</div>
				<div class="panel-heading">Error Console</div>
				<div class="panel-body">
					<textarea class="form-control code-holder lined" rows="5" id="error"></textarea>
				</div>
				
			</div>
		</div>
		</div>
	</body>
</html>
"""