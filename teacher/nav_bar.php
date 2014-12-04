<?php
	session_start();
  	include $_SERVER['DOCUMENT_ROOT'].'/db_connection.php';
	$sql_query = 'SELECT * FROM Teacher WHERE TeacherID='.$_SESSION['id'];
  	if(!$result = $db->query($sql_query)){
    	die('There was an error running the query [' . $db->error . ']');
  	}
  	while($row = $result->fetch_assoc()){
	  	$name = $row['FirstName']." ".$row['LastName'];
	}
	echo '<nav class="navbar navbar-default" role="navigation"><div class="container-fluid">';
	echo '<div class="navbar-header">';
	echo '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">';
	echo '<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span>';
	echo '<span class="icon-bar"></span><span class="icon-bar"></span>';
	echo '</button>';
	echo '<a class="navbar-brand" href="#">'.$name.'</a>';
	echo '</div><div id="navbar" class="navbar-collapse collapse">';
	echo '<ul class="nav navbar-nav">';
	if($curr_page =='user_page.php'){
		echo '<li class="active"><a href="user_page.php">Details</a></li>';
	}
	else{
		echo '<li><a href="/teacher/user_page.php">Details</a></li>';
	}
	if($curr_page =='class_admin.php'){
		echo '<li class="active"><a href="class_admin.php">Class Administration</a></li>';
	}
	else{
		echo '<li><a href="/teacher/class_admin.php">Class Administration</a></li>';
	}
	if($curr_page =='task_admin.php'){
		echo '<li class="active"><a href="task_admin.php">Task Administration</a></li>';
	}
	else{
		echo '<li><a href="task_admin.php">Task Administration</a></li>';
	}
	echo '</ul>';
	echo '<ul class="nav navbar-nav navbar-right">';
	echo '<li><a href="\logout.php"><span class="glyphicon glyphicon-log-out"></span>&nbspLog out</a></li>';
	echo '</ul></div></div>';
	echo '</nav>';
?>
