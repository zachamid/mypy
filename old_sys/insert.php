<?php
  session_start();
  include 'db_connection.php';
  $table = $_POST['table'];
  $columns = $_POST['columns'];
  $values = str_replace('\\', '', $_POST['values']);
  $sql =  "INSERT INTO ".$table."(".$columns.") VALUES (".stripslashes($values).")";
  if(!$result = $db->query($sql)){
    echo -1;
  }
  else{
  	echo mysqli_insert_id($db);
  }
?>