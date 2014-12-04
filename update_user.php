<?php
	session_start();
	include 'db_connection.php';
	$new_values = '';
	$table = $_POST['type'];
	if(isset($_POST['FirstName'])){
		$new_values.="FirstName='".$_POST['FirstName']."',";
	}
	if(isset($_POST['LastName'])){
		$new_values.="LastName='".$_POST['LastName']."',";
	}
	if(isset($_POST['Password'])){
		$new_values.="Password='".$_POST['FirstName']."',";
	}
	$sql_query = "UPDATE ".$table." SET ".substr($new_values, 0, strlen($new_values)-1)." WHERE ".$table."ID=".$_SESSION['id'];
	if(!$result = $db->query($sql_query)){
    	echo $db->error;
  	}
  	else{
  		echo '0';
  	}
?>