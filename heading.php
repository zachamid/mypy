<?php
  include 'db_connection.php';
  echo '<div class="jumbotron">';
  echo '<div class="row">';
  echo ' <div class="col-md-9">';
  echo ' <h1> MyPy</h1></br>';
  echo ' <h2> The Online Python Education Tool </h2></br>';
  echo ' </div>';
  echo ' <div class="col-md-3">';
  if(empty($_SESSION['id'])){
    echo ' <input type="email" name="email" class="form-control" id="email_field" placeholder="Email"></br>';
    echo ' <input type="password" name="pword" class="form-control" id="pword_field" placeholder="Password"></br>';
    echo ' <input type="button" value="Log In" class="btn btn-default" onclick="validate_login()">&nbsp&nbsp';
    echo ' <input type="submit" class="btn btn-default"  value="Sign Up" onclick="location.href=\'signup.php\'"></br><div id="error_space"></div> ';
  }
  else{
    $sql_query = "SELECT * FROM Student WHERE StudentID=".$_SESSION['id'];
    if(!$result = $db->query($sql_query)){
      die('There was an error running the query [' . $db->error . ']');
    }
    while($row = $result->fetch_assoc()){
      echo "Welcome</br>".$row['FirstName']." ".$row['SecondName'].'<br></br>';
    }
   echo '<form action="logout.php"><input type="Submit" value="Log Out" class="btn btn-default"></form>';
  }
  echo ' </div>';
  echo ' </div>';
  echo ' </div>';
?>
