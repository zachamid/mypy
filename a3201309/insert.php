<?php
  session_start();
  include 'db_connection.php';
  $table = $_GET['table'];
  $columns = $_GET['columns'];
  $values = stripslashes($_GET['values']);
  $sql =  "INSERT INTO ".$table."(".$columns.") VALUES (".$values.")";
  if(!$result = $db->query($sql)){
    die('There was an error running the query [' . $db->error . ']');
  }
  $_SESSION['type'] = 'Student';
  $_SESSION['id'] =mysqli_insert_id($db);
?>