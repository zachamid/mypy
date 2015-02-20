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
    	<script src="../behave.js" type="text/javascript"></script>
		<script src="../python_functions.js" type="text/javascript"></script>
		<script src="../user_functions.js" type="text/javascript"></script>
		<script src="../skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="../skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		function test_code(){
    			code = document.getElementById("model_code").value;
    			if(document.getElementById('test_check').checked){
    				code += "\\n";
    				test_cases = document.getElementById('test_cases');
    				func = document.getElementById('function').value;
    				testcases = document.getElementsByClassName('testcase');
    				descs = document.getElementsByClassName('testcase');
    				for(var test_counter = 0; test_counter < testcases.length; test_counter++){
    					desc = descs[test_counter].value;
    					test = testcases[test_counter].value;
    					
    					code += 'print "Testcase '+desc+':'+func+'('+test+')"\\n';
    					code += func+'('+test+')\\n';
    				}
    			}
    			run_code(code, 'output','error');
    		}
    		
    		function create_task(){
    			test_code();
    			error = document.getElementById('error').value;
    			if(error){
    				alert('Model Answer runs with Error')
    			}
    			else{
    				complete = document.getElementById('model_code').value;
    				skeleton = document.getElementById('skeleton_code').value;
    				result = document.getElementById('output').value;
    				title = document.getElementById('title').value;
    				task = {};
    				task["description"] = document.getElementById('description').value;
    				task["instruction"] = document.getElementById('instructions').value;
    				task["difficulty"] = document.getElementById('difficulty').value;
    				if(document.getElementById('test_check').checked){
    					task["method"] = document.getElementById('function').value;
    					task["testcase"] = [];
	    				testcases = document.getElementsByClassName('testcase');
    					descs = document.getElementsByClassName('testcase');
    					for(var test_counter = 0; test_counter < testcases.length; test_counter++){
    						testcase = {};
    						testcase['arg'] = testcases[test_counter].value;
    						testcase['description'] = testcases[test_counter].value;
    						task["testcase"].push(testcase);
    					}
    				}
    				
    				task_string = JSON.stringify(task);
    				$.ajax({
      				data : {title: title, complete: complete, skeleton: skeleton, result: result, task_xml: task_string},
      				url : '/teacher/create_task.py',
      				type : "POST",
      				dataType : "html"}).done(function(result){
      				});
      			}
    		}
    	
    		function add_row(counter){
    			var new_row = document.getElementById('test_cases').insertRow(counter);
    			new_row.insertCell(0).innerHTML='<input class="form-control description" type="text" placeholder="Description"></input>'
    			new_row.insertCell(1).innerHTML='<input class="form-control testcase" type="text" placeholder="Testcase"></input>'
    		}
	    	
    		$(document).ready(function(){
    			code_area_prep();
				var editor = new Behave({
					textarea: 		document.getElementById('model_code'),
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
    		<div class="container col-sm-6 col-md-12">
    			<div class="panel panel-default translucent">
    				<table style='width:100%'>
    					<tr><td style='width:30%'>Title</td>
    						<td>
             					<input class="form-control" type="text" id="title" placeholder="Title">
          					</td>
    					</tr>
    					<tr><td>Description</td>
    						<td>
             					<textarea class="form-control" id="description"></textarea>
          					</td>
    					</tr>
    					<tr><td>Instructions</td>
    						<td>
             					<textarea class="form-control" id="instructions"></textarea>
          					</td>
    					</tr>
    					<tr><td>Difficulty</td>
    						<td>
             					<select class="form-control" id="difficulty">
             						<option>Beginners</option>
             						<option>Easy</option>
             						<option>Intermediate</option>
             						<option>Difficult</option>
             						<option>Challenging</option>
             					</select>
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
				<div class="panel-heading">Code Skeleton</div>
				<div class='container' style="width:100%">
					<textarea rows="10" id="skeleton_code"></textarea>
				</div>
			</div>
		</div>
		
      	<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Model Code</div>
				<div class='container' style="width:100%">
					<div class="line-nums" id="line-nums"><span>1</span></div>
					<textarea class="lined" rows="10" id="model_code"></textarea>
				</div>
				<button class="form-control" 
						onclick='test_code()'
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
			</div>
		</div>
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Error Console</div>
					<div class='container' style="width:100%">
						<textarea rows="5" id="error" readonly></textarea>
					</div>
			</div>
		</div>
		<div id='debug'></div>
		<button onclick='create_task()'>Create</button>
    </body>
</html>"""
