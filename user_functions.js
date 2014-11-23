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
          end_text = 'Not a valid email address';
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

function validate_login(type_of_user){
  var table_name = type_of_user.charAt(0).toUpperCase()+type_of_user.slice(1);
  var email = document.getElementById('email_field').value;
  var pword = document.getElementById('pword_field').value;
  var data = {query: "SELECT * FROM "+table_name+" WHERE Email='"+email+"'"};
  $.ajax({
    data : data,
    url : '/run_query.php',
    type : "GET",
    dataType : "json"}).done(function(result){
    if(result.length == 0){
      document.getElementById('error_space').innerHTML = 'This Email is not a registered MyPy '+ type_of_user +'</br>You can Sign Up Now';
    }
    else{
      for(x = 0; x < result.length; x++){
	if(result[x]['Password'] == pword){
	  var login_details = {id: result[x][table_name+'ID'], type:table_name};
	  $.ajax({
	    data:login_details,
	    url: 'set_sessions.php',
	    type: 'GET',
	    dataType: "",
	    success: function(html){
	      window.location.assign('userPage.php');
	    }
	  });
	}
	else{
	  document.getElementById('error_space').innerHTML = 'Password incorrect';
	}
      }
    }
  });
}

function insert_user(table, person){
    var fields = '';
    var values = '';
    for(field in person){
    	fields += field+",";
    	values += "'"+person[field]+"',";
    }
    fields = fields.substring(0,fields.length-1);
    values = values.substring(0,values.length-1);
    var data = {query: "SELECT Email FROM Student WHERE Email=\""+person['Email']
    			+"\" UNION SELECT Email FROM Teacher WHERE Email =\""+person['Email']+"\""};
    $.ajax({
    	data : data,
        url : '/run_query.php',
        type : "GET",
        dataType : "json"}).done(function(result){
        	if(result.length != 0){
            	alert('Email is already registered');
           	}
           	else{
             	var user_detail = {table:table, values:values, columns: fields};
             	$.ajax({
               		data : user_detail,
               		url : '/insert.php',
               		type : "GET"}).done(function(id){
               			var login_credentials={id:id,type:table};
               			$.ajax({
               				data: login_credentials,
               				url: '/set_sessions.php',
               				type: 'GET'}).done(function(){
               					window.location.reload();
               			});
               	});
        	}
	});
}