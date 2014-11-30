<?php
$host = "localhost";
$user = "mbax9zh2";
$pword = "S0crat3s34!";
$table = "test";

$db = new mysqli($host, $user, $pword, $table);

if($db->connect_errno > 0){
    die('Unable to connect to database [' . $db->connect_error . ']');
}
?>
