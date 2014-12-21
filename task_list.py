#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,session, common_components,os
cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

# If new session
if session.in_session():
	cookie.load(string_cookie)
	session.print_cookie()
else:
	print 'Location:index.py'
print """Content-type: text/html\n\n

<html>
	<head>
    		<script src="jquery-1.11.1.min.js"></script>
    		<script src="user_functions.js"></script>
    		<script src="task_admin_functions.js"></script>
    		<title>Welcome</title>
    		<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    		<link href="general_style.css" rel="stylesheet">
    		<script>
    			function populate_table(tasks){
    				var table = document.getElementById('task_list');
    				var row = table.insertRow(0);
    				row.insertCell(0).innerHTML = '<b>ID</b>';
    				row.insertCell(1).innerHTML = '<b>Title</b>';
    				var counter = 1;
    				for(var task in tasks){
    					if(tasks[task]['directory'] == 1 &&
    						tasks[task]['info.xml'] == 1 &&
    						tasks[task]['task_skeleton.py'] == 1 &&
    						tasks[task]['task_complete.py'] == 1){
    						var row = table.insertRow(counter);
    						row.insertCell(0).innerHTML = "<a onclick='open_task_page("+task+")'>"+task+'</a>';
    						counter++;
    					}
    				}
    			}
    			
    			function open_task_page(taskID){
    				var mapForm = document.createElement("form");
    				mapForm.method = "POST";
    				mapForm.action = "/task_page.py";
					var mapInput = document.createElement("input");
    				mapInput.type = "text";
    				mapInput.name = "task_id";
    				mapInput.value = taskID;
    				mapForm.appendChild(mapInput);
    				document.body.appendChild(mapForm);
    				mapForm.submit();
    			}
    			
    			$( document ).ready(function() {
    				check_directory(populate_table);
				});
    		</script>
	</head>
	<body>"""
common_components.print_navbar(cookie['id'].value, 'task_list')
print """\n
			<div class="panel panel-default translucent">
      			<h3>List of Tasks</h3>
      		</div>
      		<div class="panel panel-default translucent">
      			<table id=task_list width="100%" style="border-spacing:10px">
      			</table>
      		</div>
      		<div id='task_info' class="panel panel-default translucent">
      		</div>
	</body>
</html>
"""