<?php
  include 'db_connection.php';
  $sql_query = $_GET['table'];
  if(isset($_GET['column']) && isset($_GET['criterion'];)){
    $sql_query .= " WHERE ".$_GET['column']."='".$_GET['criterion']."'";
  }
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
