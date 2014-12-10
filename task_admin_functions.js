function check_directory(data_manipulation){
	$.ajax({
		url : '/cgi-bin/read_task_information.py',
    	data: {cmd:"File_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(result){
    		console.log(result);
    		data_manipulation(result);
    	});
}
    		
function get_task_info(taskID,data_manipulation){
	$.ajax({
		url : '/cgi-bin/read_task_information.py',
    	data: {cmd:"Task_Info",params:taskID},
    	type: 'POST',
    	dataType: 'text'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_info(data_manipulation){
	$.ajax({
		url : '/cgi-bin/read_task_information.py',
    	data: {cmd:"Task_DB_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_xml(task_id, data_manipulation){
	$.ajax({
		url : '/cgi-bin/read_task_information.py',
    	data: {cmd:"Task_XML", params:task_id},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function print_object(obj) {
	ret_string="";
	for (var key in obj) {
    	if (typeof(obj[key]) == 'object') {
      		ret_string+=print_object(obj[key])+"</br>";
    	} else {
    		ret_string+="Key: " + key + " Values: " + obj[key]+"</br>";
    	}
  	}
  	return ret_string;
}