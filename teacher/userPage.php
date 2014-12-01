<?php
	session_start();
	if(empty($_SESSION['id'])){
		header('Location: index.php');
  	}
  	if($_SESSION['Type'] != 'Teacher'){
  		header('Location: ' . $_SERVER['HTTP_REFERER']);
	}
  	include '/../db_connection.php';
?>
<html>
	<head>
    	<script src="../jquery-1.11.1.min.js"></script>
    	<script src='../utils.js'></script>
    	<title>Welcome</title>
    	<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<link href="../general_style.css" rel="stylesheet">
    	<link href="teacher_style.css" rel="stylesheet">
    	<script type="text/javascript">
      
    	</script>
  	</head>
  	<body>
  		<div class="container">
  		<?php
  			$curr_page='userPage.php'
    		include 'navbar.php';
    		$sql_query = 'SELECT * FROM Teacher WHERE TeacherID='.$_SESSION['id'];
    		if(!$result = $db->query($sql_query)){
    			die('There was an error running the query [' . $db->error . ']');
  			}
  			$row = $result->fetch_assoc();
    	?>
    	<div class="container">
      		<h3>Personal Details</h3>
      		<div class="panel panel-default">
        		<table width="100%" style="border-spacing:10px">
          			<tr>
            			<td style="width:50%">
              				First Name: <input class="form-control" type="text" id="FirstName" value=<?php echo $row['FirstName'];?>>
            			</td>
            			<td>
              				<div id="FirstName_alert"></div>
            			</td>
          			</tr>
          			<tr>
            			<td style="width:50%">
              				Last Name: <input class="form-control" type="text" id="LastName" value=<?php echo $row['LastName'];?>>
            			</td>
            			<td>
              				<div id="LastName_alert"></div>
            			</td>
          			</tr>
          			<tr>
            			<td style="width:50%">
              				Email: <input class="form-control" type="text" id="Email" value=<?php echo $row['Email'];?>>
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
            				<input class="form-control" type="password" name="confirm_New_Password" placeholder="Confirm New Password">
            			</td>
            			<td>
               				<div id="confirm_New_Password_alert"></div>
            			</td>
          			</tr>
          			<tr>
         				<button class="form-control" onclick='update_user(<?php echo '"'.$_SESSION['type'].'",'.$_SESSION['id'] ?>)' type="button">
									Update
						</button>
          			</tr>
        		</table>
      		</div>
    	</div>
    	</div>
  </body>
</html>
