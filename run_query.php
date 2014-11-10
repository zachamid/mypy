<?php
  include 'db_connection.php';
  $sql_query = stripslashes($_GET['query']);
  if(!$result = $db->query($sql_query)){
    die('There was an error running the query [' . $db->error . ']');
  }
  $json_array=array();
  $counter = 0;
  while($row = $result->fetch_assoc()){
    $json_array[$counter] = $row;
    $counter++;
  }
  echo json_encode($json_array);
?>
