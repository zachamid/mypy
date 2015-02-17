#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	if cookies['type'].value == 'Student':
		print 'Location:../index.py'
else:
	print 'Location: index.py'
print """Content-type: text/html\n\n

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../user_functions.js'></script>
    	<script src='../task_admin_functions.js'></script>
    	<script src="behave.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		function add_row(counter){
    			var new_row = document.getElementById('test_cases').insertRow(counter);
    			new_row.insertCell(0).innerHTML='<input class="form-control" id="description'+counter+'" type="text" placeholder="Description"></input>'
    			new_row.insertCell(1).innerHTML='<input class="form-control" id="testcase'+counter+'" type="text" placeholder="Testcase"></input>'
    		}
	    	
    		$(document).ready(function(){
    			code_area_prep();
				var editor = new Behave({
					textarea: 		document.getElementById('code'),
					replaceTab: 	true,
				    softTabs: 		true,
				    tabSize: 		2,
			    	autoOpen: 		false,
			    	overwrite: 		false,
			    	autoStrip: 		false,
			    	autoIndent: 	false
				});
    			
    			$('#test_cases').hide();
    			$('#function').hide();
    			new_row = document.getElementById('test_cases').insertRow(0);
    			function_cell = new_row.insertCell(0);
    			function_cell.colSpan = '2';
    			function_cell.innerHTML='<input class="form-control" type="text" id="function" placeholder="Function to Run"></input>';

    			new_row = document.getElementById('test_cases').insertRow(1);
    			new_row.insertCell(0).innerHTML='<button class="form-control" id="add_testcase">Add Testcase</button>';
    			new_row.insertCell(1).innerHTML='<button class="form-control" id="remove_testcase">Remove Testcase</button>';
    		
    			$('#test_check').click(function(){
    				if(!document.getElementById('test_check').checked){
    					$('#test_cases').hide();
    					$('#function').hide();
    				}
    				else{
    					$('#test_cases').show();
    					$('#function').show();
    					if(document.getElementById('test_cases').rows.length ==1){
    						add_row(0)
    					}
    				}
    			});
    			$('#remove_testcase').click(function(){
    				if(document.getElementById('test_cases').rows.length >1){
    					$('#test_cases tr:last-child').prev('tr').remove();
    				}
    			});
    			$('#add_testcase').click(function(){
    				add_row(document.getElementById('test_cases').rows.length-1);
    			});
    		});
		</script>
    	
	</head>
	<body>"""
common_components.print_navbar_teacher(cookies['id'].value,'task_admin')
print """\n
    		<div class="container col-sm-6 col-md-9">
    			<div class="panel panel-default translucent">
    				<table style='width:100%'>
    					<tr><td style='width:30%'>Title</td>
    						<td>
             					<input class="form-control" type="text" id="Title" placeholder="Title">
          					</td>
    					</tr>
    					<tr><td>Description</td>
    						<td>
             					<textarea class="form-control" id="Description">
             					</textarea>
          					</td>
    					</tr>
    					<tr><td>Instructions</td>
    						<td>
             					<textarea class="form-control" id="Instructions">
             					</textarea>
          					</td>
    					</tr>
    					<tr><td>Add TestCases
    							<input class="form-control" id="test_check" type='checkbox' name='Test Cases'>
             					</input>
             				</td>
    						<td>
    							<table id='test_cases'></table>
          					</td>
    					</tr>
    				</table>
    			</div>
      		</div>
      		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Python Source Code</div>
				<div class='container' style="width:100%">
					<div class="line-nums" id="line-nums"><span>1</span></div>
					<textarea class="lined" rows="10" id="code"></textarea>
				</div>
				<button class="form-control" 
						onclick='run_code(document.getElementById("code").value,"output","error")'
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
</html>"""
