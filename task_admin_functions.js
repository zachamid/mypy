function check_directory(data_manipulation){
	$.ajax({
		url : '/task_directory_functions.php',
    	data: {cmd:"File_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(data_manipulation(result));
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