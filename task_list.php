<?php
	session_start();
  	if(empty($_SESSION['id']) || $_SESSION['type'] != 'Student'){
    	header('Location: index.php');
  	}
  	include 'db_connection.php';
?>

<html>
	<head>
    		<script src="jquery-1.11.1.min.js"></script>
    		<script src="user_functions.js"></script>
    		<title>Welcome</title>
    		<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    		<link href="general_style.css" rel="stylesheet">
	</head>
	<body>
		<div class="container">
			<?php
				include 'nav_bar.php'
			?>
			<div class="panel panel-default translucent">
      			<h3>List of Tasks</h3>
      		</div>
      		<div class="panel panel-default translucent">
      			<table  width="100%" style="border-spacing:10px">
      				<tr>
      					<th>TaskID</th>
      					<th>TaskName</th>
      				</tr>
      			</table>
      		</div>
		</div>
	</body>
</html>
