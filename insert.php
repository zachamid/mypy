<?php
  session_start();
  include 'db_connection.php';
  $table = $_GET['table'];
  $columns = $_GET['columns'];
  $values = str_replace('\\', '', $_GET['values']);
  $sql =  "INSERT INTO ".$table."(".$columns.") VALUES (".stripslashes($values).")";
  if(!$result = $db->query($sql)){
    die('There was an error running the query [' . $db->error . ']');
  }
  echo mysqli_insert_id($db);
?>