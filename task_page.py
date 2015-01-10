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
		<script src="behave.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
		<script>
		function correct(taskID){
    				var mapForm = document.createElement("form");
    				mapForm.method = "POST";
    				mapForm.action = "/correction_page.py";
					var taskid = document.createElement("input");
    				taskid.type = "text";
    				taskid.name = "task_id";
    				taskid.value = taskID;
    				mapForm.appendChild(taskid);
    				var code = document.createElement("input");
    				code.type = "textarea";
    				code.name = "code";
    				code.value = document.getElementById('code').value;
    				var output = document.createElement("input");
    				output.type = "textarea";
    				output.name = "output";
    				output.value = document.getElementById('output').value;
    				mapForm.appendChild(output);
    				//document.getElementById('postform').appendChild(mapForm);
    				mapForm.submit();
    			}
		
		function insert_python_content_to_code_area(result){
			if (!("Error_Title" in result)){
				document.getElementById('code').value = result['task_skeleton.py'];
			}
		}
		$(function() {
			code_area_prep();
			get_task_py("""+task_id+""",'task_skeleton.py',insert_python_content_to_code_area);
			
			var editor = new Behave({
			
				textarea: 		document.getElementById('code'),
				replaceTab: 	true,
			    softTabs: 		true,
			    tabSize: 		4,
			    autoOpen: 		false,
			    overwrite: 		false,
			    autoStrip: 		false,
			    autoIndent: 	false
			});
		});
		</script>
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
				<div class='container' style="width:100%">
					<div class="line-nums"><span>1</span></div>
					<textarea class="lined" rows="10" id="code"></textarea>
				</div>
"""
task_xml = task_delivery.get_task_xml(task_id)['task']
if('testcase' in task_xml and 'method' in task_xml):
	print """\n	<div class="panel panel-default translucent" style="width:100%">
					<table>"""
	if 'arg' in task_xml['testcase'] and 'task' in task_xml['testcase']:
		print '<tr><td>'+ task_xml['testcase']['@description']+"</td>"
		print '<td>'+ task_xml['testcase']['arg']+"</td></tr>"
	else:
		for testcase in task_xml['testcase']:
			print "			<tr>"
			print "				<td>"+ testcase['@description']+"</td>"
			print "				<td>"+ testcase['arg']+"</td>"
			print "			</tr>"		
	print """\n		</table>
			</div>
			<button class="form-control" 
	onclick='compile_code(document.getElementById("code").value,"""+task_id+""","output","error")'
     type="button">Run</button>
     <button class="form-control" 
	onclick='correct("""+task_id+""")'
     type="button">Correct</button>"""
     
else:
	print """\n
			<button class="form-control"
		onclick='run_code(document.getElementById("code").value,"output","error")' type="button">
						Run
			</button>
			<button class="form-control" onclick='correct("""+task_id+""")' type="button">
						Correct
			</button>"""
			
print """\n	</div>
		</div>
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Output</div>
				<div class='container' style="width:100%">
					<textarea rows="5" id="output" readonly></textarea>
				</div>
				<div class="panel-heading">Error Console</div>
				<div class='container' style="width:100%">
					<textarea rows="5" id="error" readonly></textarea>
				</div>
			</div>
		</div>
		<div id="postform" style="display: none;"></div>
	</body>
</html>
"""