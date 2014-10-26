<html>
<head>
<title> The World of Zac Hamid </title>
</head>
<body>
<?php
  include 'db_connection.php';
  $sql = <<<SQL
    SELECT *
    FROM `Class` 
SQL;

if(!$result = $db->query($sql)){
    die('There was an error running the query [' . $db->error . ']');
}
while($row = $result->fetch_assoc()){
    echo $row['ClassName'] . '<br />';
}
?>
</body>
</html>
