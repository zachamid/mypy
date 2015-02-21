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
student_id = cookies['id'].value
cursor = db_connection.get_connection()
new_flag = 0
curr_date = datetime.datetime.now()
task_xml = task_delivery.get_task_xml(task_id)['task']	
try:
	cursor.execute("""SELECT Attempts, ProgressID FROM Progress WHERE
					StudentID=%s AND TaskID=%s""" % (str(student_id),str(task_id)))

	if cursor.rowcount == 0:
		new_flag = 1
	else:
		progress_record = cursor.fetchone()
		cursor.execute("""UPDATE Progress SET DateModified=%s, Attempts=%d WHERE ProgressID=%s
						""" % ("'"+str(curr_date)+"'", progress_record['Attempts']+1,progress_record['ProgressID']))
except MySQLdb.Error, e:
	print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])

print """Content-type: text/html\n\n

<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<link rel="stylesheet" href="/codemirror-5.0/lib/codemirror.css">
		<script src="/codemirror-5.0/lib/codemirror.js"></script>
		<script src="/codemirror-5.0/mode/python/python.js"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
		<script>
		function correct(taskID){
			editor.save();
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
    		code.value = document.getElementById('code').value.replace(/\\r?\\n/g, '</br>');
   		 	code.value = code.value.replace(/\t/g, '&nbsp;&nbsp;&nbsp;&nbsp;');
    		//code.value = document.getElementById('code').value;
    		var output = document.createElement("input");
    		output.type = "textarea";
    		output.name = "output";
    		output.value = document.getElementById('output').value.replace(/\\r?\\n/g, '</br>');
    		output.value = output.value.replace(/\t/g, '&nbsp;&nbsp;&nbsp;&nbsp;');
    		mapForm.appendChild(output);
    		mapForm.appendChild(code);
    		document.getElementById('postform').appendChild(mapForm);
    		mapForm.submit();
		}
		$(function() {
			var editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    			lineNumbers: true,
    			mode: "python"
  			});
  			
  			$('#run').click(function(){
  				editor.save();
  				code = document.getElementById('code').value;"""
if ('testcase' in task_xml and 'method' in task_xml):
	print 'compile_code(code, %s,\'output\',\'error\');' % (str(task_id))
else:
	print 'run_code(code,\'output\',\'error\');'
print """
  			});
  			
  			$('#save').click(function(){
  				editor.save();
  				code = document.getElementById('code').value;
  				save_code(code,%s,%s);
  			});
  			
  			$('#save').click(function(){
  				correct(%s);
  			});
		});
		</script>
		<style>
			table{
				width: 100%%;
			}
		</style>
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
	<body>
"""	% (str(task_id), str(student_id), str(task_id))
common_components.print_navbar(cookies['id'].value,'')
print """\n
		<div class="col-xs-12 col-md-12 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Instruction</div>
				<div class='container' style="width:100%">
				"""+task_xml['instruction']['#text'].replace('\n','</br>')+"""\n
				</div>
			</div>
		</div>
"""
print """\n
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Python Source Code</div>
				<div class='container' style="width:100%">
					<textarea class="CodeMirror cm-s-default" rows="10" id="code">"""
if new_flag == 0:
	sql = 'SELECT Code FROM Progress WHERE StudentID=%s AND TaskID=%s' % (str(student_id),str(task_id))
	cursor.execute(sql)
	print cursor.fetchone()['Code'].replace('</br>','\n')
else:
	code = task_delivery.get_python_code_from_file(task_id, 'task_skeleton.py')['task_skeleton.py']
	cursor.execute("""INSERT INTO Progress (StudentID, TaskID, DateStarted, Code)
						Values('%s', '%s', '%s', '%s')""" % (str(student_id),str(task_id),str(curr_date),code.replace('\'','\\\'')))
	print code

print """\n				</textarea>
				</div>
"""
if('testcase' in task_xml and 'method' in task_xml):
	print """\n	<div class="panel panel-default translucent" style="width:100%">
					<table>"""
	if 'arg' in task_xml['testcase'] and 'task' in task_xml['testcase']:
		print '<tr><td>'+ task_xml['testcase']['description']['#text']+"</td>"
		print '<td>'+ task_xml['testcase']['arg']['#text']+"</td></tr>"
	else:
		for testcase in task_xml['testcase']:
			print "			<tr>"
			print "				<td>"+ testcase['description']['#text']+"</td>"
			print "				<td>"+ testcase['arg']['#text']+"</td>"
			print "			</tr>"		
	print """\n		</table>
			</div>"""
print """\n
			<table><tr><td><button class="form-control" id='run' type="button">Run</button></td>
			<td><button class="form-control" id='correct' type="button">Correct
			</button></td>"""
			
print "<td><button class=\"form-control\" id=\"save\" type=\"button\" >Save</button></td></tr></table></div>"
print		"""\n	</div>
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