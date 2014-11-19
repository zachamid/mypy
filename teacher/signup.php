<?php
	session_start();
	if(!empty($_SESSION['id']) && $_SESSION['type']=='Teacher'){
		header('Location: userPage.php');
	}
  	else if(!empty($_SESSION['id']) || $_SESSION['type']=='Student'){
  		header('Location: ' . $_SERVER['HTTP_REFERER']);
  	}
?>
<html>
  <head>
  <script src="../jquery-1.11.1.min.js"></script>
  <script src='../user_functions.js'></script>
  <title>Sign Up to MyPy</title>
  <link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="../general_style.css" rel="stylesheet">
  <link href="teacher_style.css" rel="stylesheet">
  <script>
   	function validate_detail(detail){
    	var input = document.getElementById(detail).value;
    	var end_text='';
    	var flag = 0;
    	switch(detail){
      		case 'FirstName':
      		case 'LastName':
        		if(input == ''){
          			end_text = 'Name field(s) cannot be blank';
          			flag = 1;
        		}
        		break;
      		case 'Email':
        		var at_position = input.indexOf('@');
        		var dot_position = input.lastIndexOf('.');
        		if(input == ''){
          			end_text = 'Email Field cannot be empty';
          			flag = 1;
        		}
        		else if(at_position < 1 || dot_position < at_position + 2 || dot_position + 2 > input.length){
          			end_text = 'Not a valid Email address';
          			flag = 1;
        		}
        		break;
      		case 'Password':
        		if (input == ''){
          			end_text = 'Password Field cannot be empty';
        		}
        		if (input.length < 6 || input.length > 16){
          			end_text = 'Password must be between 6 and 16 characters';
          			flag = 1;
        		}
        		break;
      		case 'confirm_Password':
        		if(input != document.getElementById('Password').value){
          			end_text = 'Passwords do not match';
          			flag = 1;
        		}
    	}
   		document.getElementById(detail+'_alert').innerHTML = end_text;
   		return flag;
  	}
  	
  	function sign_up(){
  		var fields = ['FirstName', 'LastName', 'Email','Password','confirm_Password'];
    	var flag = 0;
    	for(counter =0; counter < fields.length; counter++){
    		var out = validate_detail(fields[counter]);
      		if(out == 1){
        		flag = 1;
      		}
    	}
    	if(flag == 1){
      		alert('Please fix your form and Retry');
    	}
    	else{
    		var teacher = {};
    		for(counter=0; counter<fields.length-1;counter++){
    			teacher[fields[counter]]=document.getElementById(fields[counter]).value;
    		}
    		insert_user('Teacher',teacher);
    	}
  	}
  </script>
  </head>
  <body>
    <?php include 'heading.php'; ?>
    
    <div class="container"><div class="panel panel-default translucent"><h3>Teacher Sign Up</h3></div><div class="panel panel-default translucent">
      <h4>Teacher Details</h4>
      <table width="100%" style="border-spacing:10px">
        <tr>
          <td style="width:50%">
             <input class="form-control" type="text" id="FirstName" placeholder="First Name" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="FirstName_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="text" id="LastName" placeholder="Last Name" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="LastName_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="text" id="Email" placeholder="Email Address" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="Email_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="password" id="Password" placeholder="Password" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="Password_alert"></div>
          </td>
        </tr>
        <tr>
          <td style="width:50%">
            <input class="form-control" type="password" id="confirm_Password" placeholder="Confirm Password" onblur='validate_detail(this.id)'>
          </td>
          <td>
             <div id="confirm_Password_alert"></div>
          </td>
        </tr>
      </table>
    </div></div>
    <div class="container">
      <input type="button" value="Submit" class="btn btn-default" onclick="sign_up()">
    </div>
    &nbsp
  </body>
</html>		
