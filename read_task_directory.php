<?php

include 'db_connection.php';
$sql_query = "SELECT * FROM Task";
if(!$result = $db->query($sql_query)){
	die('There was an error running the query [' . $db->error . ']');
}

$file_existance_matrix = array();
$dir = "../tasks";
while($row = $result->fetch_assoc()){
	$file_existance_matrix[$row['TaskID']] = array();
	$dir_list = scandir($dir);
	if(in_array($row['TaskID'], $dir_list))
	{
		$file_existance_matrix[$row['TaskID']]['directory']=1;
		$dir_list = scandir($dir.DIRECTORY_SEPARATOR.$row['TaskID']);
		echo print_r($dir_list);
		if(in_array('task_skeleton.py',$dir_list)){
			$file_existance_matrix[$row['TaskID']]['task_skeleton.py']=1;
		}
		else{
			$file_existance_matrix[$row['TaskID']]['task_skeleton.py']=0;
		}
		if(in_array('info.xml',$dir_list)){
			$file_existance_matrix[$row['TaskID']]['info.xml']=1;
		}
		else{
			$file_existance_matrix[$row['TaskID']]['info.xml']=0;
		}
		if(in_array('task_complete.py',$dir_list)){
			$file_existance_matrix[$row['TaskID']]['task_complete.py']=1;
		}
		else{
			$file_existance_matrix[$row['TaskID']]['task_complete.py']=0;
		}
	}
	else{
		$file_existance_matrix[$row['TaskID']]['directory']=0;
	}
}

echo json_encode($file_existance_matrix);
?>