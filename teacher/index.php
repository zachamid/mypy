<?php
	if(strcmp($_SESSION['type'],'Student')==0){
  		header('Location: ' . $_SERVER['HTTP_REFERER']);
	}
	/*if(!empty($_SESSION['id'])){
		header('Location: userPage.php');
	}*/
	session_start();
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
    	echo $_SESSION['type']. '   '.$_SESSION['id'];
    	if($_SESSION['type']=='Teacher'){
	  		include 'teacher/navbar.php'; 
	  	}
	  	else{
	  		include 'heading.php';
	  	} 
	?>
  </body>
</html>
