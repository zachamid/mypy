<?php
$host = 'mysql17.000webhost.com';
$user = 'a3201309_mypy';
$pword = 'socrates34';
$table =  'a3201309_mypy';

$db = new mysqli($host, $user, $pword, $table);

if($db->connect_errno > 0){
    die('Unable to connect to database [' . $db->connect_error . ']');
}
?>