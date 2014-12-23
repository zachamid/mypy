#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os,datetime
import task_delivery
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
cursor = db_connection.get_connection()
try:
	cursor.execute("""SELECT * FROM Progress WHERE
					StudentID=%s AND TaskID=%s""",(cookies['id'].value,task_id))

	if cursor.rowcount == 0:
		cursor.execute("""INSERT INTO Progress (StudentID, TaskID)
						Values(%s, %s)""",(cookies['id'].value,task_id))
	else:
		progress_record = cursor.fetchone()
		curr_date = datetime.datetime.now()	
		cursor.execute("""UPDATE Progress
						SET DateModified=%s
						WHERE ProgressID=%s
						""",(curr_date, progress_record['ProgressID']))
except MySQLdb.Error, e:
	print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])

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
"""

task_xml = task_delivery.get_task_xml(task_id)
print task_xml
if('testcase' in task_xml and 'method' in task_xml):
	print """\n<div class="container col-md-6 col-sm-12"><div class="panel panel-default translucent" style="width:100%"><table>"""
	for testcase in task_xml['testcase']:
		print "<tr>"
		print "<td>"+ testcase['@description']+"</td>"
		print "<td>"+ testcase['arg']+"</td></tr></br>"
	print """\n<button class="form-control" onclick='compile_code(document.getElementById("code").value"""+task_id+""","output","error")'
     type="button">Run</button>"""
else:
	print """\n
		<button class="form-control"
		onclick='run_code(document.getElementById("code").value,"output","error")' type="button">
						Run
					</button>"""
print """\n		</div>
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