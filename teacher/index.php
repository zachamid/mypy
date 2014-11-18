<?php
	session_start();
	if($_SESSION['Type'] == 'Student'){
  		header('Location: ' . $_SERVER['HTTP_REFERER']);
	}
?>
<html>
  <head>
    <script src="../jquery-1.11.1.min.js"></script>
    <title>Welcome</title>
    <link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    <script src='../user_functions.js'></script>
  </head>
  <body>
    <?php include 'heading.php'; ?>
  </body>
</html>
