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
  			function getClasses(select_id){
    			var data = {cmd: "Classes"};
    			$.ajax({
      				data : data,
      				url : '/admin_queries.py',
      				type : "POST",
      				dataType : "json"}).done(function(result){
      					var class_select = document.getElementById(select_id);
      					for(counter=0;counter<result.length; counter++){
        					var new_option = new Option(result[counter]['ClassName'],result[counter]['ClassID']);
        					class_select.options[counter] = new_option;
      					}
    				});
 			}
 			
 			function getTeacherList(){
 				var data = {cmd: "TeacherList"};
 				$.ajax({
 					data: data,
 					url: '/admin_queries.py',
 					type: "POST",
 					dataType: "json"}).done(function(result){
 						teacherList = document.getElementById('teacherList');
 						console.log(result);
 						for (row_count=teacherList.rows.length-1;row_count >=0; row_count--){
 							teacherList.deleteRow(row_count);	
 						}
 						if(result.length !=0){
 							row_counter = 0
 							var currentRow = teacherList.insertRow(row_counter);
 							row_counter++;
 							var currClass = result[0][ClassID];
 							currentRow.insertCell(0).innerHTML='<b>'+result[0][ClassName]+'</b>';
 							var currentCell = currentRow.insertCell(1);
	 						for(counter = 1; counter<result.length; counter++){
	 							if(currClass != result[counter][ClassID]){
	 								currentRow=teacherList.insertRow(row_counter);
	 								currentRow.insertCell(0).innerHTML='<b>'+result[counter][ClassName]+'</b>';
	 								currentCell=currentRow.insertCell(1);
	 								row_counter++;
	 							}
	 							currentCell+=result[counter][FirstName]+' '+result[counter][LastName]+'</br>';
	 						}
	 					}
 				});
 			}
 			
 			function getClassList(){
 				class_select = document.getElementById('classes');
 				class_ID = class_select.options[class_select.selectedIndex].value;
 				var data = {cmd: "ClassList",ClassID:''+class_ID};
 				var table = document.getElementById('classList');
 				row_no = table.rows.length;
 				for (row_count=row_no-1;row_count >=0; row_count--){
 					table.deleteRow(row_count);	
 				}
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
    					header_row.insertCell(5).innerHTML = '';
    					var counter = 1;
    					for (student in result){
    						var row = table.insertRow(counter);
    						row.insertCell(0).innerHTML = result[student]['StudentID'];
    						row.insertCell(1).innerHTML = result[student]['FirstName'];
    						row.insertCell(2).innerHTML = result[student]['LastName'];
    						row.insertCell(3).innerHTML = result[student]['Email'];
    						row.insertCell(4).innerHTML = '<a onclick="removeFromClass('+result[student]['StudentID']+')">Remove from class</a>';
    						row.insertCell(5).innerHTML = "<a onclick='deleteStudent("+result[student]['StudentID']+")'>Delete</a>";
    						counter++;
    					}
    				});
 			}
 			
 			function getUnassignedList(){
 				var data = {cmd: "ClassList",ClassID:'-1'};
 				var table = document.getElementById('unassignedList');
 				row_no = table.rows.length;
 				for (row_count=row_no-1;row_count >=0; row_count--){
 					table.deleteRow(row_count);	
 				}
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
    					header_row.insertCell(5).innerHTML = '';
    					var counter = 1;
    					for (student in result){
    						var row = table.insertRow(counter);
    						row.insertCell(0).innerHTML = result[student]['StudentID'];
    						row.insertCell(1).innerHTML = result[student]['FirstName'];
    						row.insertCell(2).innerHTML = result[student]['LastName'];
    						row.insertCell(3).innerHTML = result[student]['Email'];
    						row.insertCell(4).innerHTML = "<select id='classSelect"+result[student]['StudentID']+"'></select>";
    						row.insertCell(4).innerHTML += "<button onclick=''>Assign</button>"
    						row.insertCell(5).innerHTML = "<a onclick='deleteStudent("+result[student]['StudentID']+")'>Delete</a>";
    						getClasses('classSelect'+result[student]['StudentID']);
    						counter++;
    					}
    				});
 			}
 			
 			function insertClass(){
 				class_name = document.getElementById('className').value;
 				data = {table:'Class',columns:'ClassName',values:'"'+class_name+'"'};
 				$.ajax({
      				data : data,
      				url : '/insert.py',
      				type : "POST",
      				dataType : "text"}).done(function(result){
      				});
 			}
 			
 			function deleteStudent(id){
 				var conf = window.confirm("Are you sure you want to delete this Student");
 				if(conf == true){
	 				data = {table:'Student',id:''+id};
	 				$.ajax({
	      				data : data,
	      				url : '/delete.py',
	      				type : "POST",
	      				dataType : "text"}).done(function(result){
	      					getClassList();
	      					getUnassignedList();
	      				});
	 			}
 			}
 					
 			function removeFromClass(studentID){
 				data = {id: studentID,
 						type: 'Student',
 						ClassID: '-1'};
 				$.ajax({
      				data : data,
      				url : '/update.py',
      				type : "POST",
      				dataType : "text"}).done(function(result){
      					getClassList();
      				});
 			}
 			
  			$(function() {
  				getUnassignedList();
  				getTeacherList();
  			});
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
						<td>
							<input type="text" id="className">
						</td>
          				<td>
          					<button onclick='insertClass()'>Add Class</button>
          				</td>
					</tr>
				</table>
			</div><br>
			<div class="panel panel-default translucent">
				Edit Class Lists
				</br>
				<select class="form-control" id="classes" 
				onchange="getClassList()"
				onfocus="getClasses('classes')"></select>
				</br>
				<div>
					<table id='classList'>
					</table>
				</div>
			</div>
			<div class="panel panel-default translucent">
				Assign Unassigned Students
				</br>
				<div>
					<table id='unassignedList'>
					</table>
				</div>
			</div>
		</div></div>
		<div class="container col-sm-12 col-md-12">
			<div class="panel panel-default translucent">
				<table id='teacherList'></table>
			</div>
		</div>
	</body>
</html>
"""