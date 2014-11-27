<?php
  session_start();
  $_SESSION['id'] = $_POST['id'];
  $_SESSION['type'] = $_POST['type'];
  echo $_SESSION['type'].' : '.$_SESSION['id'];
?>