<?php
	session_start();
	if(empty($_SESSION['id'])){
		header('Location: index.php');
  	}
  	include '../db_connection.php';
?>
<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../user_functions.js'></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		$( document ).ready(function() {
    			check_directory();
			});
			
    		function check_directory(){
    			$.ajax({
    				url : '/read_task_directory.php',
    				dataType: 'json'}).done(function(tasks){
    					var table = document.getElementById('task_list');
    					var counter = 1;
    					for(var task in tasks){
    						console.log(task);
    						var row = table.insertRow(counter);
    						var id = row.insertCell(0).innerHTML = task;
    						if(tasks[task]['directory'] == 1){
    							var id = row.insertCell(1).innerHTML = '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>';
    						}
    						else{
    							var id = row.insertCell(1).innerHTML = '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
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
    					}
    			});
    		}
    	</script>
	</head>
	<body>
		<div class="container">
			<?php
  				$curr_page='taskAdmin.php';
    			include 'navbar.php';
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
      				<div class="panel panel-default translucent">
      					<table id="task_list" width="100%" style="border-spacing:10px">
      						<tr>
      							<th>TaskID</th>
      							<th>Directory</th>
      							<th>task_skeleton.py</th>
      							<th>task_complete.py</th>
      							<th>info.xml</th>
      						</tr>
      					</table>
      				</div>
      			</div>
      		</div>
    	</div>
    </body>
</html> 