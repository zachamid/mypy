#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,session, common_components,os
cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

# If new session
if session.in_session():
	cookie.load(string_cookie)
	print 'Location:\'user_page.py\''
print """Content-type: text/html\n\n

<html>
	<head>
  		<script src="jquery-1.11.1.min.js"></script>
  		<script src='user_functions.js'></script>
  		<title>Sign Up to MyPy</title>
  		<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  		<link rel="stylesheet" type="text/css" href="general_style.css">
  		<script>
   			$(document).ready(function(){
     			var data = {cmd: "Schools"};
       				$.ajax({
         				data : data,
         				url : 'run_query.py',
         				type : "POST",
         				dataType : "json"}).done(function(result){
           					var school_select = document.getElementById('schools');
           					for(counter=0;counter<result.length; counter++){
             					var new_option = new Option(result[counter]['School'],counter+1);
             					school_select.options[school_select.options.length] = new_option;
           					}
           					getClasses(school_select.options[school_select.selectedIndex].text);
         				});
   			})

  			function getClasses(){
    			var school_select = document.getElementById('schools');
    			var school = school_select.options[school_select.selectedIndex].text;
    			var data = {cmd: "Classes", param:school};
    			$.ajax({
      				data : data,
      				url : 'run_query.py',
      				type : "POST",
      				dataType : "json"}).done(function(result){
      					var class_select = document.getElementById('classes');
      					for(counter=0;counter<result.length; counter++){
        					var new_option = new Option(result[counter]['ClassName'],result[counter]['ClassID']);
        					class_select.options[counter] = new_option;
      					}
    				});
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
    				var student = {};
    				for(counter=0; counter<fields.length-1;counter++){
    					student[fields[counter]]=document.getElementById(fields[counter]).value;
    				}
    				student['ClassID'] = document.getElementById('classes').options[document.getElementById('classes').selectedIndex].value;
					insert_user('Student',student);
    			}
  			}
  		</script>
  	</head>
  	<body>
  		<div class='container'>"""
commmon_components.print_header()
    
print """\n
    	<div class="container"><div class="panel panel-default translucent"><h3>Student Sign Up</h3></div><div class="panel panel-default translucent">
    		<h4>Student Details</h4>
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
    	<div class="container"><div class="panel panel-default translucent">
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
    	</div>&nbsp</div>
  	</body>
</html>	"""
