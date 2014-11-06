<?php
  include 'db_connection.php';
  $column = $_GET['column'];
  $condition = $_GET['criterion'];
  $table = $_GET['table'];
  $sql_query = $table;
  if(isset($condition) && isset($column)){
    $sql_query .= " WHERE ".$column."='".$condition."'";
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