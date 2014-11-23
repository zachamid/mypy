<?php
	session_start();
?>
<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="python_functions.js" type="text/javascript"></script>
    	<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
	</head>
	<body>
		<div class="container">
		<?php
			$curr_page = 'playground.php';
			if($_SESSION['type']=='Student'){
				include('navbar.php');
			}
			else if($_SESSION['type']=='Teacher'){
				include('teacher/navbar.php');
			}
			else{
				include('heading.php');
			}
		?>
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Python Source Code</div>
				<div class="panel-body">
					<textarea class="form-control code-holder" rows="10" id="code">
for i in range(8):
 print i
					</textarea>
					<button class="form-control" onclick='run_code("code","output")' type="button">
						Run
					</button>
				</div>
			</div>
		</div>
		<div class="col-xs-12 col-md-6 col-sm-12">
			<div class="panel panel-default translucent">
				<div class="panel-heading">Output</div>
				<div class="panel-body">
					<textarea class="form-control code-holder" rows="10" id="output"></textarea>
				</div>
			</div>
		</div>
		</div>
	</body>
</html>