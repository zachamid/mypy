<?php
	session_start();
	if(empty($_SESSION['id'])){
		header('Location: index.php');
  	}
  	if($_SESSION['Type'] != 'Teacher'){
  		header('Location: ' . $_SERVER['HTTP_REFERER']);
	}
  	include getcwd().'/../db_connection.php';
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
      $(document).ready(function(){
        var data = {query: "SELECT * FROM Teacher WHERE TeacherID="+<?php echo $_SESSION['id'];?>};
        $.ajax({
          data : data,
          url : '/run_query.php',
          type : "GET",
          dataType : "json"}).done(function(result){
            for(i=0; i<result.length; i++){
              document.getElementById('first_name').value= result[i]['FirstName'];
              document.getElementById('last_name').value= result[i]['LastName'];
              document.getElementById('email').value= result[i]['Email'];
            }
          });
        });
    </script>
  </head>
  <body>
    <?php include 'heading.php'; ?>
    <div class="container">
      <h3>Personal Details</h3>
      <div class="panel panel-default">
        <table width="100%" style="border-spacing:10px">
          <tr>
            <td style="width:50%">
              First Name: <input class="form-control" type="text" name="first_name" id="first_name" placeholder="First Name">
            </td>
          </tr>
          <tr>
            <td style="width:50%">
              Last Name: <input class="form-control" type="text" name="last_name" id="last_name" placeholder="First Name">
            </td>
          </tr>
          <tr>
            <td style="width:50%">
              Email: <input class="form-control" type="text" name="email" id="email" placeholder="Email Address">
            </td>
            <td>
              <div id="email_alert"></div>
            </td>
          </tr>
          <tr>
            <td style="width:50%">
              <input class="form-control" type="password" name="old_pword" placeholder="Old Password">
            </td>
            <td>
               <div id="pword_alert"></div>
            </td>
          </tr>
          <tr>
            <td style="width:50%">
              <input class="form-control" type="password" name="pword" placeholder="New Password">
            </td>
            <td>
               <div id="pword_alert"></div>
            </td>
          </tr>
          <tr>
            <td style="width:50%">
              <input class="form-control" type="password" name="confirm_pword" placeholder="Confirm New Password">
            </td>
            <td>
               <div id="confirm_pword_alert"></div>
            </td>
          </tr>
          <tr>
            <td style="width:50%">
               <div id="class_place"></div>
            </td>
          </tr>
        </table>
      </div>
    </div>
    <div class="container">
      <h3>Tasks</h3>
      <div class="panel panel-default">
        <table id="task_list" width="100%" style="border-spacing:10px">
          <tr>
           <th>ID</th><th>Task</th><th>Date Started</th><th>Last Opened</th><th>Date Completed</th>
          </tr>
        </table>
      </div>
    </div>
  </body>
</html>
