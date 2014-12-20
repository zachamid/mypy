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
	print 'Location:\'index.py\''
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
    						row.insertCell(0).innerHTML = "<a onclick='get_xml_data("+task+")'>"+task+'</a>';
    						counter++;
    					}
    				}
    			}
    			
    			function get_xml_data(taskID){
    				var info_area = document.getElementById('task_info');
    				info_area.innerHTML = 'Loading Information...';
    				
    				get_task_xml(taskID, function(xml_info){
    					info_area.innerHTML = print_object(xml_info);
    				});
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