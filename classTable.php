<?php
	session_start();
  	if(empty($_SESSION['id']) || $_SESSION['type'] != 'Student'){
    	header('Location: index.php');
  	}
  	include 'db_connection.php';
?>
<html>
	<head>
    	<script src="jquery-1.11.1.min.js"></script>
    	<script src="user_functions.js"></script>
    	<title>Welcome</title>
    	<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="general_style.css" rel="stylesheet">
    </head>
    <body>
  		<div class="container">
  			<?php
 		 		$curr_page = 'classTable.php';
 		 		include 'navbar.php';
 		 		$sql_query = 'SELECT Class.ClassName,Class.ClassID FROM Student INNER JOIN Class ON Student.ClassID=Class.ClassID WHERE StudentID='.$_SESSION['id'];
 		 		if(!$result = $db->query($sql_query)){
    				die('There was an error running the query [' . $db->error . ']');
  				}
  				$row = $result->fetch_assoc()
 		 		$classID = $row['ClassID'];
 		 	?>
 		 	<div class="container" style="width:100%">
      			<div class="panel panel-default translucent">
      				<table id="task_list" width="100%" style="border-spacing:10px">
          				<tr>
          					<th>ID</th>
          					<th>Name</th>
          					<th>Points</th>
          				</tr>
          				<?php
          					$sql_query = 'SELECT StudentID, FirstName, LastName FROM Student WHERE ClassID='.$classID;
          					if(!$result = $db->query($sql_query)){
    							die('There was an error running the query [' . $db->error . ']');
  							}
  							while($row=$result->fetch_assoc()){
  								echo '<tr>'
  								if($row['StudentID'] == $_SESSION['id']){
  									echo '<td><b>'.$row['StudentID'].'</b></td>';
  									echo '<td><b>'.$row['FirstName'].' '.$row['LastName'].'</b></td>';
  									echo '<td><b>#</b></td>';
  								}
  								else{
  									echo '<td>'.$row['StudentID'].'</td>';
  									echo '<td>'.$row['FirstName'].' '.$row['LastName'].'</td>';
  									echo '<td>#</td>';
  								}
  								echo '</tr>'
  							}
          				?>
          			</table>
      			</div>
      		</div>
 		 </div>
</html>