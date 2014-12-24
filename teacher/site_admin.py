#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components,db_connection

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
cursor = db_connection.get_connection()
print 'Content-type: text/html'
if cookies.has_key('id') and cookies.has_key('type'):
	print cookies
	if cookies['type'].value == 'Teacher':
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value)
		record = cursor.fetchone()
		if record['Administrator'] == 0:
			print 'Location:index.py'
	else:
		print 'Location:../index.py'
else:
	print 'Location:../index.py'
	
print """\n\n

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
  		<script src='../user_functions.js'></script>
  		<title>Teacher Portal: Site Administration</title>
  		<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  		<link href="../general_style.css" rel="stylesheet">
  		<link href="teacher_style.css" rel="stylesheet">
  		<script>
  			function getClasses(){
    			var data = {cmd: "Classes"};
    			$.ajax({
      				data : data,
      				url : '/admin_queries.py',
      				type : "POST",
      				dataType : "json"}).done(function(result){
      					var class_select = document.getElementById('classes');
      					for(counter=0;counter<result.length; counter++){
        					var new_option = new Option(result[counter]['ClassName'],result[counter]['ClassID']);
        					class_select.options[counter] = new_option;
      					}
    				});
 			}
 			
 			function getClassList(){
 				class_select = document.getElementById('classes');
 				class_ID = class_select.options[class_select.selectedIndex];
 				var data = {cmd: "ClassList",param1:class_ID};
 				var table = document.getElementById('classList');
 				$.ajax({
      				data : data,
      				url : '/admin_queries.py',
      				type : "POST",
      				dataType : "json"}).done(function(result){
      					var header_row = table.insertRow(0);
    					header_row.insertCell(0).innerHTML = '<b>ID</b>';
    					header_row.insertCell(1).innerHTML = '<b>First Name</b>';
    					header_row.insertCell(2).innerHTML = '<b>Last Name</b>';
    					header_row.insertCell(3).innerHTML = '<b>Email</b>';
    					header_row.insertCell(4).innerHTML = '';
    					var counter = 0;
    					for (student in result){
    						var row = table.insertRow(counter);
    						row.insertCell(0).innerHTML = result['StudentID'];
    						row.insertCell(0).innerHTML = result['FirstName'];
    						row.insertCell(0).innerHTML = result['LastName'];
    						row.insertCell(0).innerHTML = result['Email'];
    						row.insertCell(0).innerHTML = 'Delete';
    					}
    				});
 			}
 		</script>
	</head>
	<body>"""
common_components.print_navbar_teacher(cookies['id'].value, 'site_admin')
print """\n
		<div class="container col-sm-12 col-md-12">
			<div class="panel panel-default translucent">
				Class Administration
			</div></br>
			<div class="panel panel-default translucent">
				Add Class</br>
				<table>
					<tr>
						<td>Class Name:</td>
					</tr>
					<tr>
						<td>
							<input type="text" name="className">
						</td>
          				<td>
          					<button>
          						Add Class
          					</button>
          				</td>
					</tr>
				</table>
			</div><br>
			<div class="panel panel-default translucent">
				Edit Class Lists
				</br>
				<select class="form-control" id="classes" 
				onchange="getClassList()"
				onfocus="getClasses()"></select>
				</br>
				<div id='classListDiv'>
					<table id='classList'>
					</table>
				</div>
			</div>
		</div></div>
		<div class="container col-sm-12 col-md-12">
			<div class="panel panel-default translucent">
				Teacher Administration
			</div>
		</div>
	</body>
</html>
"""