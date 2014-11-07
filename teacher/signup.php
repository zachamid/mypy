<?php
  session_start();
  if(!empty($_SESSION['id'])){
    header('Location: userPage.php');
  }
?>
<html>
  <head>
  <script src="../jquery-1.11.1.min.js"></script>
  <script src='../utils.js'></script>
  <title>Sign Up to MyPy</title>
  <link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="../gen.css" rel="stylesheet">
  <script>
   $(document).ready(function(){
     var data = {table: "SELECT DISTINCT School FROM Class"};
       $.ajax({
         data : data,
         url : 'thirdyearproject/run_query.php',
         type : "GET",
         dataType : "json"}).done(function(result){
           var school_select = document.getElementById('schools');
           for(counter=0;counter<result.length; counter++){
             var new_option = new Option(result[counter]['School'],counter+1);
             school_select.options[school_select.options.length] = new_option;
           }
           getClasses(school_select.options[school_select.selectedIndex].text);
         });
   })
  
  function validate_detail(detail){
    var input = document.getElementById(detail).value;
    var end_text='';
    var flag = 0;
    switch(detail){
      case 'first_name':
      case 'last_name':
        if(input == ''){
          end_text = 'Name field(s) cannot be blank';
          flag = 1;
        }
        break;
      case 'email':
        var at_position = input.indexOf('@');
        var dot_position = input.lastIndexOf('.');
        if(input == ''){
          end_text = 'Email Field cannot be empty';
          flag = 1;
        }
        else if(at_position < 1 || dot_position < at_position + 2 || dot_position + 2 > input.length){
          end_text = 'Not a valid email address';
          flag = 1;
        }
        break;
      case 'pword':
        if (input == ''){
          end_text = 'Password Field cannot be empty';
        }
        if (input.length < 6 || input.length > 16){
          end_text = 'Password must be between 6 and 16 characters';
          flag = 1;
        }
        break;
      case 'confirm_pword':
        if(input != document.getElementById('pword').value){
          end_text = 'Passwords do not match';
          flag = 1;
        }
    }
   document.getElementById(detail+'_alert').innerHTML = end_text;
   return flag;
  }

  function getClasses(){
    var school_select = document.getElementById('schools');
    var school = school_select.options[school_select.selectedIndex].text;
    var data = {table: "SELECT * FROM Class", column:"School",criterion: school};
    $.ajax({
      data : data,
      url : 'run_query.php',
      type : "GET",
      dataType : "json"}).done(function(result){
      var class_select = document.getElementById('classes');
      for(counter=0;counter<result.length; counter++){
        var new_option = new Option(result[counter]['ClassName'],result[counter]['ClassID']);
        class_select.options[counter] = new_option;
      }
    });
  }
  </script>
  </head>
  <body>
    <?php include 'heading.php'; ?>
    
    <div class="container"><h3>Student Sign Up</h3><div class="panel panel-default">
      <h4>Student Details</h4>
      <table width="100%" style="border-spacing:10px">
        <tr>
          <td style="width:50%">
             <input class="form-control" type="text" id="first_name" placeholder="First Name" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="first_name_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="text" id="last_name" placeholder="Last Name" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="last_name_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="text" id="email" placeholder="Email Address" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="email_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="password" id="pword" placeholder="Password" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="pword_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="password" id="confirm_pword" placeholder="Confirm Password" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="confirm_pword_alert"></div>
          </td>
        </tr>
      </table>
    </div></div>
    <div class="container"><div class="panel panel-default">
      <h4>Class Details</h4></br>
      <table width="100%" style="border-spacing:10px">
        <tr><td style="width:50%">
          <select class="form-control" id="schools" onchange="getClasses()"></select>
        </td><td>&nbsp</td></tr>
        <tr><td style="width:50%">
          <select class="form-control" id="classes">
            <option>Select a school</option>
          </select>
        </td><td>&nbsp</td></tr>
      </table>
    </div></div>
    <div class="container">
      <input type="button" value="Submit" class="btn btn-default" onclick="sign_up()">
    </div>
    &nbsp
  </body>
</html>		
