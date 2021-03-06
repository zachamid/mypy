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
    			var header_row = table.insertRow(0);
    			header_row.insertCell(0).innerHTML = '<b>ID</b>';
    			header_row.insertCell(1).innerHTML = '<b>Directory</b>';
    			header_row.insertCell(2).innerHTML = '<b>task_skeleton.py</b>';
    			header_row.insertCell(3).innerHTML = '<b>task_complete.py</b>';
    			header_row.insertCell(4).innerHTML = '<b>info.xml</b>';
    			var counter = 1;
    			
    			for(var task in tasks){
    				console.log("Entered the function");
    				var row = table.insertRow(counter);
    				row.insertCell(0).innerHTML = task;
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
			
    		$( document ).ready(function() {
    			check_directory(populate_table);
    			get_task_info(function(result){
    				for (var field in result){
    					document.getElementById('task_info').innerHTML+=result[field]+'</br>';
    				}
    			});
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
</html> 
