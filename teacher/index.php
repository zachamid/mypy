<?php
	session_start();
	if($_SESSION['type']=='Student'){
  		header('Location:'.$_SERVER['HTTP_HOST']);
	}
	/*if(!empty($_SESSION['id'])){
		header('Location: userPage.php');
	}*/
?>
<html>
  <head>
    <script src="../jquery-1.11.1.min.js"></script>
    <link href="../general_style.css" rel="stylesheet">
    <link href="teacher_style.css" rel="stylesheet">
    <title>Welcome</title>
    <link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    <script src='../user_functions.js'></script>
  </head>
  <body>
    <?php 
    	echo var_dump($_SESSION['type']=='Teacher');
    	if($_SESSION['type']=='Teacher'){
	  		include 'teacher/navbar.php'; 
	  	}
	  	else if (empty($_SESSION['id'])){
	  		include 'heading.php';
	  	} 
	?>
  </body>
</html>
