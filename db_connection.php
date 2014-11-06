<?php
$host = "dbhost.cs.man.ac.uk";
$user = "mbax9zh2";
$pword = "socrates34";
$table = "mbax9zh2";

$db = new mysqli($host, $user, $pword, $table);

if($db->connect_errno > 0){
    die('Unable to connect to database [' . $db->connect_error . ']');
}
?>
