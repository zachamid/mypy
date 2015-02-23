#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
cursor = db_connection.get_connection()

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
		<script>
		$(function() {
			var editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    			lineNumbers: true,
    			mode: "python"
  			});
  			
  			$('#run').click(function(){
  				editor.save();
  				code = document.getElementById('code').value;
  				run_code(code,"output","error");
  			});
  			$('#load_tutorial').click(function(){
  				tutorial_id = document.getElementById('tutorials').value;
  				$.ajax({
    			data : {cmd:'Get_Tutorial', tutorial_id: tutorial_id},
		    	url : '/read_task_information.py',
    			type : "POST",
    			dataType : "text"}).done(function(result){
    				editor.setValue(result);
		    	});
  			});
  			
		});
		</script>
		<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
	</head>
	<body>"""

if not (cookies.has_key('id') and cookies.has_key('type')):
	common_components.print_header()
else:
	if cookies['type'].value == "Student":
		common_components.print_navbar(cookies['id'].value,'playground')
	else:
		common_components.print_navbar_teacher(cookies['id'].value,'playground')

print """\n
		<div class="col-xs-12 col-md-12 col-sm-12"><div class="panel panel-default translucent">
			<table style='padding:2px;width:100%'>
				<tr>
					<td style='padding:5px;width:80%'>
						<select class="form-control" id='tutorials'>
"""
sql = 'SELECT TutorialID, TutorialName FROM Tutorial'
cursor.execute(sql)
tutorials = cursor.fetchall()
for tutorial in tutorials:
	print '<option value=\''+str(tutorial['TutorialID'])+'\'>'
	print tutorial['TutorialName']
	print '</option>'
print """\n
						</select>
					</td>
					<td style='padding:5px;width:20%'>
						<button class="form-control" id="load_tutorial">Load</button>
					</td>
				</tr>
			</table>
		</div></div>
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Python Source Code</div>
				<div class='container' style="width:100%">
					<textarea class = 'CodeMirror cm-s-default' rows="10" id="code"></textarea>
				</div>
				<button class="form-control" id='run'
						 type="button">
						Run
					</button>
			</div>
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
	</body>
</html>
"""