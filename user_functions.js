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
        break;
      case 'new_Password':
      	if (input == ''){
          end_text = 'Password Field cannot be empty';
        }
        if (input.length < 6 || input.length > 16){
          end_text = 'Password must be between 6 and 16 characters';
          flag = 1;
        }
        break
      case 'confirm_New_Password':
      	if(input != document.getElementById('new_Password').value){
          end_text = 'Passwords do not match';
          flag = 1;
        }
        break;
    }
	document.getElementById(detail+'_alert').innerHTML = end_text;
	return flag;
}

function validate_login(type_of_user){
	var email = document.getElementById('email_field').value;
	var pword = document.getElementById('pword_field').value;
  	var data = {email: email, password:pword, type:type_of_user};
  	$.ajax({
    	data : data,
    	url : 'login_validation.py',
    	type : "POST",}).done(function(result){
    	if(result.indexOf("-1") > -1){
    		document.getElementById('error_space').innerHTML = 'Incorrect Email-Password Combination';
    	}
    	else{
    		/*var login_details = {cmd:'set',type:type_of_user, id:result};
    		$.ajax({
	    		data:login_details,
	    		url: 'session.py',
	    		type: 'POST',
	    		success: function(html){
	    			//window.location.assign('user_page.py');
	    			window.location.reload();
	    		}
	  		});*/
	  		document.cookie = "type="+type_of_user+";secure";
	  		window.location.reload();
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
    var data = {cmd: 'CheckEmail', param:person['Email']};
    $.ajax({
    	data : data,
        url : '/run_query.php',
        type : "POST",
        dataType : "json"}).done(function(result){
        	if(result.length != 0){
            	alert('Email is already registered');
           	}
           	else{
             	var user_detail = {table:table, values:values, columns: fields};
             	$.ajax({
               		data : user_detail,
               		url : '/insert.php',
               		type : "POST"}).done(function(id){
               			if(id != -1){
	               			var login_credentials={id:id,type:table};
    	           			$.ajax({
        	       				data: login_credentials,
            	   				url: '/set_sessions.php',
               					type: 'POST'}).done(function(){
               						window.location.reload();
               				});
               			}
               	});
        	}
	});
}

function update_user(type_of_user, id){
	var fields = ['FirstName', 'LastName','Password','new_Password','confirm_New_Password'];
    var flag = [];
    for(counter =0; counter < fields.length; counter++){
    	flag[counter] = validate_detail(fields[counter]);
    	console.log(flag[counter]);
    }
    if(flag.indexOf(0) == -1){
    	alert('Please fix your form and Retry');
    }
    else{
    	
    	$.ajax({
    		data : {email: document.getElementById('Email').value,
    				password:document.getElementById('Password').value,
    				type:type_of_user},
    		url : '/login_validation.php',
    		type : "POST",}).done(function(login_result){
    			var user = {};
    			if(flag[0]==0){
    				user['FirstName']=document.getElementById('FirstName').value;
    			}
    			if(flag[1]==0){
    				user['LastName']=document.getElementById('LastName').value;
    			}
    			if(flag[3] == 0 && flag[4] ==0){
    				user['Password'] = document.getElementById('new_Password').value;
    			}
    			user['type'] = type_of_user;
    			if(login_result != '-1'){
    				$.ajax({
						data:user,
						url: '/update_user.php',
						type: 'POST'}).done(function(update_result){
							if(update_result=='0'){
								window.location.reload();
							}
							else{
								alert(update_result);
							}
					});
				}
				else{
					document.getElementById('Password_alert').innerHTML = 'Password Incorrect';
				}
			});
	}
}

function clear_cookies(){
	var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
    	var cookie = cookies[i];
    	var eqPos = cookie.indexOf("=");
    	var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    	document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
    window.location.reload();
}