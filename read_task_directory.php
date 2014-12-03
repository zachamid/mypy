<html>
<body>
<?php
function dirToArray($dir) { 
   
   $result = array(); 

   $cdir = scandir($dir); 
   foreach ($cdir as $key => $value) 
   { 
      if (!in_array($value,array(".",".."))) 
      { 
         if (is_dir($dir . DIRECTORY_SEPARATOR . $value)) 
         { 
            $result[$value] = dirToArray($dir . DIRECTORY_SEPARATOR . $value); 
         } 
         else 
         { 
            $result[] = $value; 
         } 
      } 
   } 
   
   return $result; 
} 

include 'db_connection.php';
$sql_query = "SELECT * FROM Task";
if(!$result = $db->query($sql_query)){
	die('There was an error running the query [' . $db->error . ']');
}

$file_existance_matrix = array();
$dir = "../tasks";
while($row = $result->fetch_assoc()){
	$file_existance_matrix_single = array();
	$dir_list = scandir($dir);
	if(in_array($row['TaskID'], $dir_list))
	{
		$file_existance_matrix_single['directory']=1;
		echo $row['Title'].': Directory is there</br>';
		$dir_list = scandir($dir1.DIRECTORY_SEPARATOR.$row['TaskID']);
		if(in_array('task_skeleton.py',$dir_list)){
			echo $row['Title'].': task_skeleton.py present</br>';
			$file_existance_matrix_single['task_skeleton.py']=1;
		}
		else{
			echo $row['Title'].': task_skeleton.py not present</br>';
			$file_existance_matrix_single['task_skeleton.py']=0;
		}
		if(in_array('info.xml',$dir_list)){
			echo $row['Title'].': info.xml present</br>';
			$file_existance_matrix_single['info.xml']=1;
		}
		else{
			echo $row['Title'].': info.xml not present</br>';
			$file_existance_matrix_single['info.xml']=0;
		}
		if(in_array('task_complete.py',$dir_list)){
			echo $row['Title'].': task_complete.py present</br>';
			$file_existance_matrix_single['task_complete.py']=1;
		}
		else{
			echo $row['Title'].': task_complete.py not present</br>';
			$file_existance_matrix_single['task_complete.py']=0;
		}
	}
	else{
		echo $row['Title'].': Directory is not there</br>';
		$file_existance_matrix_single['directory']=1;
	}
	$file_existance_matrix[$row['TaskID']] = $file_existance_matrix_single;
}

echo json_encode(file_existance_matrix);
?>
</body>
</html>