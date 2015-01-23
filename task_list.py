#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os, task_delivery
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
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
    		</script>
	</head>
	<body>"""
common_components.print_navbar(cookies['id'].value, 'task_list')
print """\n
		<div class="col-xs-12 col-md-12 col-sm-12">
			<div class="panel panel-default translucent">
      			<h3>List of Tasks</h3>
      		</div>
      		<div class="panel panel-default translucent">
      			<table id=task_list width="100%" style="border-spacing:10px">
      				<tr><th><b>ID</b></th>
      					<th><b>Title</b></th></tr>
      			"""
cursor = db_connection.get_connection()
file_info = task_delivery.get_file_info()
for task in file_info:
	if(file_info[task]['directory'] == 1 
	and file_info[task]['task_complete.py'] == 1
	and file_info[task]['task_skeleton.py'] == 1 
	and file_info[task]['info.xml'] == 1):
		cursor.execute('SELECT * FROM Task WHERE TaskID='+str(task))
		task_info = cursor.fetchone()
		print "<tr><td><a onclick='open_task_page("+str(task)+")'>"+str(task)+'</a></td><td>'+task_info['Title']+'</td></tr>'
      	print """\n
      			</table>
      		</div>
      	</div>
	</body>
</html>
"""