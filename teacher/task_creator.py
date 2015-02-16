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
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		function add_row(counter){
    			var new_row = $('#test_cases').insertRow(counter);
    			new_row.insertCell(0).innerHTML='<input class="form-control testcase" type="text"></input>'
    			new_row.insertCell(1).innerHTML='<button class="form-control" id="remove_testcase">Remove</button>'
    		}
	    	
    		$(document).ready(function(){
    			$('#test_check').click(function(){
    				if($('#test_check').checked){
    					$('#test_cases').hide();
    				}
    				else{
    					$('#test_cases').show();
    					if(document.getElementById('test_cases').rows.length ==0){
    						add_row(0)
    					}
    				}
    			});
    			$('#remove_testcase').click(function(){
    				$(this).parent().parent().remove();
    			});
    			$('#add_testcase').click(function(){
    				add_row(document.getElementById('test_cases').rows.length);
    			});
    		});
    	</script>
    	
	</head>
	<body>"""
common_components.print_navbar_teacher(cookies['id'].value,'task_admin')
print """\n
    		<div class="container col-sm-6 col-md-9">
    			<div class="panel panel-default translucent">
    				<table>
    					<tr><td>Title</td>
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
    					<tr><td>Add TestCases</td>
    						<td>
             					<input class="form-control" id="test_check" type='checkbox'>
             					</input></br>
             					<table id='test_cases'></table>
             					<button class="form-control" id='add_testcase'>
          					</td>
    					</t>
    				</table>
    			</div>
      		</div>
    </body>
</html>"""
