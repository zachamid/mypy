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
    	<script src='../utils.js'></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script>
    		function check_directory(){
    			$.ajax({
    				url : '/read_task_directory.php'}).done(function(result){
    					
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
      					<h3>Classes Managed</h3>
      				</div>
      				<div class="panel panel-default translucent">
      					<table id="task_list" width="100%" style="border-spacing:10px">
      						<tr>
      							<th>TaskID</th>
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