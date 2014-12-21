#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	if cookies['type'] == 'Teacher':
		print 'Location: index.py'
else:
	print 'Location: index.py'

task_info = cgi.FieldStorage()
task_id = task_info['task_id'].value

print """Content-type: text/html\n\n

<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="jquery-linedtextarea.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
		<script>
		function insert_python_content_to_code_area(result){
			if (!("Error_Title" in result)){
				document.getElementById('code').value = result['task_skeleton.py'];
			}
		}
		
		$(function() {
			$(".lined").linedtextarea({selectedLine: 1});
		});
		$( document ).ready(function() {
			get_task_py("""+task_id+""",'task_skeleton.py',insert_python_content_to_code_area);
		});
		</script>
		<link rel="stylesheet" type="text/css" href="jquery-linedtextarea.css">
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
	</head>
	<body>
"""		
common_components.print_navbar(cookies['id'].value,'')
print """\n
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Python Source Code</div>
				<div class="panel-body">
					<textarea class="lined" cols="80" rows="10" id="code"></textarea>
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
					<textarea class="lined" cols="80" rows="5" id="output"></textarea>
				</div>
				<div class="panel-heading">Error Console</div>
				<div class="panel-body">
					<textarea class="lined" cols="80" rows="5" id="error"></textarea>
				</div>			
			</div>
		</div>
	</body>
</html>
"""