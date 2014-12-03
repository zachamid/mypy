<html>
<body>
<?php
include 'db_connection.php';
$sql_query = "SELECT * FROM Task";
if(!$result = $db->query($sql_query)){
	die('There was an error running the query [' . $db->error . ']');
}

$dir1 = "../tasks";
$dir_list = scandir($dir1);
while($row = $result->fetch_assoc()){
	if(in_array($row['TaskID'], $dir_list)){
		echo $row['TaskName'].': Directory not there</br>';
	}
}

print_r($dir_list);
?>
</body>
</html>