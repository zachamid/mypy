<?php
  	include 'db_connection.php';
  	$sql_cmd = $_POST['cmd'];
  	$sql_query = '';
  	if($sql_cmd == 'Schools'){
  		$sql_query="SELECT DISTINCT School FROM Class";
  	}
  	if($sql_cmd == 'Classes'){
  		$sql_query = 'SELECT * FROM Class WHERE School="'.$_POST['param'].'"';
   	}
   	if($sql_cmd == 'Progress'){
   		$sql_query = 'SELECT * FROM Progress WHERE StudentID='.$_POST['param'];
   	}
   	if($sql_cmd == 'CheckEmail'){
   		$sql_query = 'SELECT Email FROM Student WHERE Email=\''.$_POST['param'];
   		$sql_query .="' UNION SELECT Email FROM Teacher WHERE Email='"+$_POST['param']."'";
   	}
  	if(!$result = $db->query($sql_query)){
    	die('There was an error running the query [' . $db->error . ']');
  	}
  	$json_array=array();
  	$counter = 0;
  	while($row = $result->fetch_assoc()){
    	$json_array[$counter] = $row;
    	$counter++;
  	}
  	echo json_encode($json_array);
?>
