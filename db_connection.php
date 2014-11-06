<?php
$database_host = "dbhost.cs.man.ac.uk";
$database_user = "mbax9zh2";
$database_pass = "socrates34";
$database_name = "mbax9zh2";

$db = new mysqli($host, $user, $pword, $table);

if($db->connect_errno > 0){
    die('Unable to connect to database [' . $db->connect_error . ']');
}
?>
