<?php
  include 'db_connection.php';
  echo '<div class="jumbotron" style="background:LightBlue ">';
  echo '<div class="row">';
  echo ' <div class="col-md-9">';
  echo ' <h1> MyPy</h1></br>';
  echo ' <h2> The Online Python Education Tool </h2></br>';
  echo ' </div>';
  echo ' <div class="col-md-3">';
  if(empty($_SESSION['id'])){
    echo ' <input type="email" name="email" class="form-control" id="email_field" placeholder="Email"></br>';
    echo ' <input type="password" name="pword" class="form-control" id="pword_field" placeholder="Password"></br>';
    echo '<button type="button" class="btn btn-default btn-sm" onclick="validate_login(\'student\')">';
  	echo '<span class="glyphicon glyphicon-log-in"></span> Login';
	echo '</button>&nbsp&nbsp';
	echo '<button type="button" class="btn btn-default btn-sm" onclick="location.href=\'signup.php\'">';
  	echo '<span class="glyphicon glyphicon-user"></span> Sign Up';
	echo '</button>';
    echo '</br><div id="error_space"></div> ';
  }
  else{
    $sql_query = "SELECT * FROM Student WHERE StudentID=".$_SESSION['id'];
    if(!$result = $db->query($sql_query)){
      die('There was an error running the query [' . $db->error . ']');
    }
    while($row = $result->fetch_assoc()){
      echo "<h3>Welcome</br><b>".$row['FirstName']." ".$row['SecondName'].'</b><br></br></h3>';
    }
   	echo '<form action="logout.php">';
   	echo '<button type="submit" class="btn btn-default btn-sm">';
  	echo '<span class="glyphicon glyphicon-log-out"></span> Sign Out';
	echo '</button></form>';
  }
  echo ' </div>';
  echo ' </div>';
  echo ' </div>';
?>
