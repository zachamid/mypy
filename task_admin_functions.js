function check_directory(data_manipulation){
	$.ajax({
		url : '/cgi-bin/read_task_information.py',
    	data: {cmd:"File_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(result){
    		console.log("BLACKBOX");
    		data_manipulation(result)
    	});
}
    		
function get_task_info(taskID){
	$.ajax({
		url : '/task_directory_functions.php',
    	data: {cmd:"Task_Info",params:taskID},
    	type: 'POST',
    	dataType: 'text'}).done(function(tasks){
    			document.getElementById('task_info').innerHTML=tasks;
    });
}