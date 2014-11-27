<?php
	session_start();
	include 'db_connection.php';
	$email = $_POST['email'];
	$password = $_POST['password'];
	$type = $_POST['type'];
	if($type == 'Student'){
		$sql_query =  "SELECT * FROM Student WHERE Email=\"".$email."\"";
		if(!$result = $db->query($sql_query)){
    		die('There was an error running the query [' . $db->error . ']');
  		}
  		if(mysqli_num_rows($result) == 0){
  			echo "-1";
  		}
  		else{
  			$row = $result->fetch_assoc();
  			if($row['Password'] == $password){
	  			echo $row['StudentID'];
	  		}
	  		else{
	  			echo "-1";
	  		}
  		}
	}
	if($type == 'teacher'){
		$sql_query =  "SELECT * FROM Teacher WHERE Email=\"".$email."\"";
		if(!$result = $db->query($sql_query)){
    		die('There was an error running the query [' . $db->error . ']');
  		}
  		if(mysqli_num_rows($result) == 0){
  			echo "-1";
  		}
  		else{
  			$row = $result->fetch_assoc();
  			if($row['Password'] == $password){
	  			echo $row['TeacherID'];
	  		}
	  		else{
	  			echo "-1";
	  		}
  		}
	}
?>