<?php
  session_start();
  if(empty($_SESSION['id'])){
    header('Location: index.php');
  }
  include 'db_connection.php';
?>
<html>
  <head>
    <script src="jquery-1.11.1.min.js"></script>
    <script src='utils.js'></script>
    <title>Welcome</title>
    <link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="gen.css" rel="stylesheet">
    <script type="text/javascript">
      $(document).ready(function(){
        var data = {table: "SELECT * FROM Student", condition:<?php echo $_SESSION['id'];?>, column: "StudentID"};
        $.ajax({
          data : data,
          url : 'run_query.php',
          type : "GET",
          dataType : "json"}).done(function(result){
            for(i=0; i<result.length; i++){
              document.getElementById('first_name').value= result[i]['FirstName'];
              document.getElementById('last_name').value= result[i]['SecondName'];
              document.getElementById('email').value= result[i]['Email'];
              var data = {table: "SELECT * FROM Class", condition:result[i]['ClassID'], column: "ClassID"};
              $.ajax({
                data : data,
                url : 'run_query.php',
                type : "GET",
                dataType : "json"}).done(function(result2){
                  for(j=0; j<result2.length; j++){
                    document.getElementById('class_place').innerHTML= "Class: " + result2[j]['ClassName'];
                  }
              });
              data ={table: "SELECT * FROM Task INNER JOIN Progress ON Progress.TaskID=Task.TaskID", column: "Progress.StudentID", criterion: <?php echo $_SESSION['id'];?>}
              $.ajax({
                data : data,
                url : 'run_query.php',
                type : "GET",
                dataType : "json"}).done(function(result2){
                  var tasktable = document.getElementById('task_list');
                  for(j=0; j<result2.length; j++){
                    var row = tasktable.insertRow(j+1);
                    var taskID = row.insertCell(0);
                    var taskName = row.insertCell(1);
                    var started = row.insertCell(2);
                    var modified = row.insertCell(3);
                    var completed = row.insertCell(4);
                    taskID.innerHTML = result2[j]['TaskID'];
                    taskName.innerHTML = result2[j]['Title'];
                    started.innerHTML = result2[j]['DateStarted'];
                    modified.innerHTML = result2[j]['DateModified'];
                    completed.innerHTML = result2[j]['DateCompleted'];
                  }
              });
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
