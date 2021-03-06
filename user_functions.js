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
    	url : '/login_validation.py',
    	type : "POST"}).done(function(id){
    	id = id.trim();
    	if(id.indexOf("-1") > -1){
    		document.getElementById('error_space').innerHTML = 'Incorrect Email-Password Combination';
    	}
    	else{
    		set_cookies(type_of_user,id);
	  		window.location.reload();
		}
	
 	});
}

function insert_user(table, person){
    var data = {cmd: 'CheckEmail', Email:person['Email']};
    $.ajax({
    	data : data,
        url : '/admin_queries.py',
        type : "POST",
        dataType : "json"}).done(function(result){
        	if(result.length != 0){
            		alert('Email is already registered');
           	}
           	else{
             	var user_detail = {FirstName: person['FirstName'],
				   LastName: person['LastName'],
				   Email: person['Email'],
				   Password: person['Password'],
				   Table: table};
             	$.ajax({
               		data : user_detail,
               		url : '/insert_user.py',
               		type : "POST",
               		dataType : "json"}).done(function(result){
               			set_cookies(table,result['id']);
               			window.location.reload()
               	});
        	}
	});
}

function update_user(type_of_user, id){
	var fields = ['FirstName', 'LastName','Password','new_Password','confirm_New_Password'];
    var flag = [];
    for(counter =0; counter < fields.length; counter++){
    	flag[counter] = validate_detail(fields[counter]);
    }
    if(flag.indexOf(0) == -1){
    	alert('Please fix your form and Retry');
    }
    else{
    	
    	$.ajax({
    		data : {email: document.getElementById('Email').value,
    				password:document.getElementById('Password').value,
    				type:type_of_user},
    		url : '/login_validation.py',
    		type : "POST",}).done(function(login_result){
    			var user = {};
    			user['id']=id;
    			user['type']=type_of_user;
    			if(flag[0]==0){
    				user['FirstName']=document.getElementById('FirstName').value;
    			}
    			if(flag[1]==0){
    				user['LastName']=document.getElementById('LastName').value;
    			}
    			if(flag[3] == 0 && flag[4] ==0){
    				user['Password'] = document.getElementById('new_Password').value;
    			}
    			if(login_result != '-1'){
    				$.ajax({
						data:user,
						url: '/update.py',
						type: 'POST'}).done(function(update_result){
							if(update_result.trim()=='1'){
								window.location.reload();
							}
							else{
								alert('Could not update');
							}
					});
				}
				else{
					document.getElementById('Password_alert').innerHTML = 'Password Incorrect';
				}
			});
	}
}

function set_cookies(type_of_user,id){
	document.cookie = "type="+type_of_user+";path=/";
	document.cookie = "id="+id+";path=/";
}

function clear_cookies(){
	var cookies = document.cookie.split(";");
	document.cookie = "id=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
	document.cookie = "type=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
	document.cookie = "id=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/teacher";
	document.cookie = "type=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/teacher";
    window.location.reload();
    
}

/* Copied from w3schools */
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}