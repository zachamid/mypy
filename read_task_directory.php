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

$dir = "../tasks";
while($row = $result->fetch_assoc()){
	$dir_list = scandir($dir1);
	if(in_array($row['TaskID'], $dir_list))
	{
		echo $row['Title'].': Directory is there</br>';
		$dir_list = scandir($dir1.DIRECTORY_SEPARATOR.$row['TaskID']);
		if(in_array('task_skeleton.py',$dir_list)){
			echo $row['Title'].': task_skeleton.py present</br>';
		}
		else{
			echo $row['Title'].': task_skeleton.py not present</br>';
		}
		if(in_array('info.xml',$dir_list)){
			echo $row['Title'].': info.xml present</br>';
		}
		else{
			echo $row['Title'].': info.xml not present</br>';
		}
		if(in_array('task_complete.py',$dir_list)){
			echo $row['Title'].': task_complete.py present</br>';
		}
		else{
			echo $row['Title'].': task_complete.py not present</br>';
		}
	}
	else{
		echo $row['Title'].': Directory is not there</br>';
	}
}

print_r($dir_list);
?>
</body>
</html>