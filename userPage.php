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
  		$curr_page = 'userPage.php';
  		include 'navbar.php'; 
	  	$sql_query = 'SELECT * FROM Student INNER JOIN Class ON Student.ClassID=Class.ClassID WHERE StudentID='.$_SESSION['id'];
  		if(!$result = $db->query($sql_query)){
    		die('There was an error running the query [' . $db->error . ']');
  		}
  		$row = $result->fetch_assoc()
  	?>
    	<div class="container col-sm-6 col-md-9">
    		<div class="container" style="width:100%">
    			
      			<div class="panel panel-default translucent">
      			<h3>Personal Details</h3></div>
      			<div class="panel panel-default translucent">
        			<table width="100%" style="border-spacing:10px">
          				<tr>
            				<td style="width:50%">
              					First Name: <input class="form-control" type="text" id="FirstName" value=<?php echo $row['FirstName']; ?> >
            				</td>
            				<td>
              					<div id="FirstName_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					Last Name: <input class="form-control" type="text" id="LastName" value=<?php echo $row['LastName']; ?> >
            				</td>
            				<td>
              					<div id="LastName_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					Email: <input class="form-control" type="text" id="Email" value=<?php echo $row['Email']; ?> readonly>
            				</td>
            				<td>
              					<div id="Email_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					<input class="form-control" type="password" id="Password" placeholder="Old Password">
            				</td>
            				<td>
               					<div id="Password_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					<input class="form-control" type="password" id="new_Password" placeholder="New Password">
            				</td>
            				<td>
               					<div id="new_Password_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
              					<input class="form-control" type="password" id="confirm_New_Password" placeholder="Confirm New Password">
            				</td>
            				<td>
               					<div id="confirm_New_Password_alert"></div>
            				</td>
          				</tr>
          				<tr>
            				<td style="width:50%">
               					<div id="class_place"><?php echo $row['ClassName']; ?></div>
            				</td>
            				<td>
            					<button class="form-control" onclick='update_user(<?php echo '"'.$_SESSION['type'].'",'.$_SESSION['id'] ?>)' type="button">
									Update
								</button>
            				</td>
          				</tr>
        			</table>
      			</div>
    		</div>
    		<div class="container" style="width:100%">
      			<div class="panel panel-default translucent"><h3>Tasks</h3></div>
      			<div class="panel panel-default translucent">
        			<table id="task_list" width="100%" style="border-spacing:10px">
          				<tr>
           					<th>ID</th>
           					<th>Task</th>
           					<th>Date Started</th>
           					<th>Last Opened</th>
           					<th>Date Completed</th>
          				</tr>
          				<?php
          					$sql_query = 'SELECT * FROM Progress INNER JOIN Task ON Progress.TaskID=Task.TaskID WHERE Progress.StudentID='.$_SESSION['id'];
          					if(!$result = $db->query($sql_query)){
    							die('There was an error running the query [' . $db->error . ']');
  							}
  							while($row = $result->fetch_assoc()){
  								print "<tr>";
  								print "<td>".$row['TaskID']."</td>";
  								print "<td>".$row['TaskName']."</td>";
  								print "<td>".$row['DateStarted']."</td>";
  								print "<td>".$row['DateModified']."</td>";
  								print "<td>".$row['DoteCompleted']."</td>";
  								print "</tr>";
  							}
          				?>
        			</table>
      			</div>
    		</div>
    	</div></div>
  	</body>
</html>
