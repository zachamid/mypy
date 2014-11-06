<?php
  session_start();
  $_SESSION['id'] = $_GET['id'];
  $_SESSION['type'] = $_GET['type'];
  echo $_SESSION['type'];
  echo $_SESSION['email'];
?>