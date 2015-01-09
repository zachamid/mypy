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
student_id = cookies['id'].value
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
		<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<style>
			table,td,th, tr {
    			border: 1px solid black;
			}
		</style>
    </head>
	<body>
"""
common_components.print_navbar(cookies['id'].value,'')
codetocorrect = code.replace('</br>','\n')
codetocorrect = codetocorrect.replace('&nbsp;&nbsp;&nbsp;&nbsp;','\t')
print """\n
		<div class="container">
      		<div class="panel panel-default">
      			<table style="width:100%">
      				<tr>
      					<td colspan="2">
      					<div class='container' style="width:100%">
							<textarea class="lined" rows="10" id="code" readonly>
"""
print task_delivery.get_compile_code(task_id, codetocorrect)
print """\n				</textarea></div></div>
						</td>
					</tr>
					<tr>
						<td>
							Correctness
						</td>
						<td>
"""
print task_correction.judge_correctness(task_id,student_id,codetocorrect)
print """\n 			</td>
					</tr>
					<tr>
						<td>
							Similarity to Model Answer
						</td>
						<td>"""
#print task_correction.judge_similarity(task_id, codetocorrect)
print """/n				</td>
					</tr>
					<tr>
						<td>
							Time
						</td>
						<td>
"""
print task_correction.judge_time(task_id,codetocorrect)
print """\n 			</td>
					</tr>
					<tr>
						<td>
							Attempts
						</td>
						<td>"""
task_correction.judge_attempts(task_id, codetocorrect)
print """/n				</td>
					</tr>
				</table>
"""

print """\n
		</div></div>
	</body>
</html>
"""