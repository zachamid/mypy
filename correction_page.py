#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os,datetime
import task_delivery, task_correction
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	if cookies['type'] == 'Teacher':
		print 'Location: index.py'
	else:
		print cookies
else:
	print 'Location: index.py'

task_info = cgi.FieldStorage()
task_id = task_info['task_id'].value
code = task_info['code'].value
cursor = db_connection.get_connection()

print """Content-type: text/html\n\n

<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="behave.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
		<script></script>
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
	<body>
"""
print code
print """

"""
task_correction.judge_correctness(task_id, code.replace('</br>','\n'))
print """

"""

task_correction.judge_similarity(task_id, code.replace('</br','\n'))
"""\n
	</body>
</html>
"""