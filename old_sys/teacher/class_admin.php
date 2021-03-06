

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../utils.js'></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
	</head>
	<body>
		<div class="container">
			<?php
  				$curr_page='class_admin.php';
    			include 'nav_bar.php';
    			$sql_query = 'SELECT * FROM Teacher WHERE TeacherID='.$_SESSION['id'];
    			if(!$result = $db->query($sql_query)){
    				die('There was an error running the query [' . $db->error . ']');
  				}
  				$row = $result->fetch_assoc();
    		?>
    		<div class="container col-sm-6 col-md-9">
    			<div class="container" style="width:100%">
    				<div class="panel panel-default translucent">
      					<h3>Classes Managed</h3>
      				</div>
      				<div class="panel panel-default translucent">
      					<table>
      						<?php
      							$sql_query = "SELECT * FROM Class INNER JOIN TeacherClassRelationship ON Class.ClassID=TeacherClassRelationship.ClassID WHERE TeacherID=".$_SESSION['id'];
    							if(!$result = $db->query($sql_query)){
    								die('There was an error running the query ['.$db->error.']');
  								}
  								while($row = $result->fetch_assoc()){
  									echo "<tr>";
  									echo "<td>".$row['ClassID']."</td>";
  									echo "<td>".$row['ClassName']."</td>";
  									echo "<td>".$row['School']."</td>";
  									echo "<td>Remove</td>";
  									echo "</tr>";
  								}
      						?>
      					</table>
      					
      				</div>
      				<div class="panel panel-default translucent">
      					<h3>Student Progress</h3>
      				</div>
      				<div class="panel panel-default translucent">
      					<table id="classList">
      						Still in Progress
      					</table>
      				</div>
      			</div>
      		</div>
		</div>
	</body>
</html>
