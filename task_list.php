<?php
	session_start();
  	if(empty($_SESSION['id']) || $_SESSION['type'] != 'Student'){
    	header('Location: index.php');
  	}
  	include 'db_connection.php';
?>
