<?php
	session_start();
	if(empty($_SESSION['id']) || $_SESSION['type']=='Student'){
		header("Location:http://".$host."/");
  	}
  	include '../db_connection.php';
?>
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
    			console.log("Entered the function");
    			var counter = 1;
    			for(var task in tasks){
    				console.log("Entered the function");
    				var row = table.insertRow(counter);
    				var id = row.insertCell(0);
    				var content = document.createTextNode(task);
    				id.appendChild(content);
    				if(tasks[task]['directory'] == 1){
    					var directory = row.insertCell(1);
    					var content = document.createTextNode('<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>');
						directory.appendChild(content);
    				}
    				else{
    					var directory = row.insertCell(1)
    					var content = document.createTextNode('<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>');
    					directory.appendChild(content);
    				}
    				if(tasks[task]['task_skeleton.py'] == 1){
    					var id = row.insertCell(2).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
    					var id = row.insertCell(2).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
    				}
    				if(tasks[task]['task_complete.py'] == 1){
    					var id = row.insertCell(3).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
    					var id = row.insertCell(3).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
    				}
    				if(tasks[task]['info.xml'] == 1){
						var id = row.insertCell(4).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    				}
    				else{
						var id = row.insertCell(4).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
					}
    				counter++;
    			}
			}
			
    		$( document ).ready(function() {
    			check_directory(populate_table);
    			get_task_info("1");
			});
    	</script>
	</head>
	<body>
		<div class="container">
			<?php
  				$curr_page='task_admin.php';
    			include 'nav_bar.php';
    			$sql_query = 'SELECT * FROM Teacher WHERE TeacherID='.$_SESSION['id'];
    			if(!$result = $db->query($sql_query)){
    				die('There was an error running the query [' . $db->error . ']');
  				}
  				$row = $result->fetch_assoc();
    		?>
    		
    		<div class="container col-sm-6 col-md-9">
    			<div class="container" style="width:100%">
    				<div class="panel panel-default translucent">
      					<h3>Task List</h3>
      				</div>
      				<div class="panel panel-default translucent" style="max-height:60px;overflow:auto;width:1000px">
      				<table id="task_list" style="border-spacing:10px;">
      					<thead><tr>
      						<th>TaskID</th>
      						<th>Directory</th>
      						<th>task_skeleton.py</th>
      						<th>task_complete.py</th>
      						<th>info.xml</th>
      					</tr></thead>
      					<tbody></tbody>
      				</table>
      				</div>
      				<div class="panel panel-default translucent" id="task_info">
      				</div>
      			</div>
      		</div>
    	</div>
    </body>
</html> 
