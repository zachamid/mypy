#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import session,common_components

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

if session.in_session():
	cookie.load(string_cookie)
	session.print_cookie()
	if cookie['type'].value == 'Student':
		print 'Location:../index.py'
else:
	print 'Location: index.py'
print """Content-type: text/html\n\n

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../user_functions.js'></script>
    	<script src='../task_admin_functions.js'></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		function populate_table(tasks){
    			var table = document.getElementById('task_list');
    			var header_row = table.insertRow(0);
    			header_row.insertCell(0).innerHTML = '<b>ID</b>';
    			header_row.insertCell(1).innerHTML = '<b>Directory</b>';
    			header_row.insertCell(2).innerHTML = '<b>task_skeleton.py</b>';
    			header_row.insertCell(3).innerHTML = '<b>task_complete.py</b>';
    			header_row.insertCell(4).innerHTML = '<b>info.xml</b>';
    			var counter = 1;
    			
    			for(var task in tasks){
    				var row = table.insertRow(counter);
    				row.insertCell(0).innerHTML = "<a onclick='show_XML_info("+task+")'>"+task+"</a>";
    				if(tasks[task]['directory'] == 1){
    					row.insertCell(1).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
    					row.insertCell(1).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
    				}
    				if(tasks[task]['task_skeleton.py'] == 1){
    					row.insertCell(2).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
    					row.insertCell(2).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
    				}
    				if(tasks[task]['task_complete.py'] == 1){
    					row.insertCell(3).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
    					row.insertCell(3).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
    				}
    				if(tasks[task]['info.xml'] == 1){
						row.insertCell(4).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
						row.insertCell(4).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
					}
    				counter++;
    			}
			}
			
			function show_XML_info(task_id){
				get_task_xml(task_id,function(result){
    				var task_info = document.getElementById("task_info");
    				task_info.innerHTML =print_object(result);
    			});
			}
			
    		$( document ).ready(function() {
    			check_directory(populate_table);
			});
    	</script>
	</head>
	<body>
		<div class="container">"""
common_components.print_navbar_teacher(cookie['id'].value,'task_admin')
print """\n
    		<div class="container col-sm-6 col-md-9">
    			<div class="container" style="width:100%">
    				<div class="panel panel-default translucent">
      					<h3>Task List</h3>
      				</div>
      				<div class="panel panel-default translucent" style="max-height:60px;overflow:auto;">
      					<table id="task_list" style="border-spacing:10px;">
      					
      					</table>
      				</div>
      				<div class="panel panel-default translucent" id="task_info">
      				</div>
      			</div>
      		</div>
    	</div>
    </body>
</html>"""
