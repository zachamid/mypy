<?php
	session_start();
	include 'db_connection.php';
	$table = $_POST['type'];
	$fName = $_POST['FirstName'];
	$lName = $_POST['LastName'];
	$pWord = $_POST['Password'];
	$sql_query = "UPDATE ".$table." SET FirstName='".$fName."',LastName='".$lName."', Password='".$pWord."' WHERE ".$table."ID=".$_SESSION['id'];
	if(!$result = $db->query($sql_query)){
    	echo $db->error;
  	}
  	else{
  		echo '0';
  	}
?>