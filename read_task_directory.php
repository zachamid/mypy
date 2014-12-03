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

$dir1 = "../tasks";
$dir_list = scandir($dir1);
while($row = $result->fetch_assoc()){
	if(in_array($row['TaskID'], $dir_list)){
		echo $row['TaskName'].': Directory is there</br>';
	}
	else{
		echo $row['Title'].': Directory is not there</br>';
	}
}

print_r($dir_list);
?>
</body>
</html>