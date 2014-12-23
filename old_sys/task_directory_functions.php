<?php
$cmd = $_POST['cmd'];
switch($cmd){
	case "File_Info":
		retrieve_file_info();
		break;
	case "Task_Info":
		retrieve_task_info($_POST['params']);
		break;
}

function retrieve_file_info(){
	include 'db_connection.php';
	$sql_query = "SELECT * FROM Task ORDER BY TaskID ASC";
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
}

function retrieve_task_info($taskID){
	$xml_path = "../tasks/".$taskID."/info.xml";
	if(!$task_info = simplexml_load_file($xml_path)){
		die("-1");
	}
	echo json_encode($task_info);
}
?>