function check_directory(data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"File_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(result){
    		data_manipulation(result);
    	});
}
    		
function get_task_info(taskID,data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Task_Info",params:taskID},
    	type: 'POST',
    	dataType: 'text'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_info(data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Task_DB_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_xml(task_id, data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Task_XML", params:task_id},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function print_xml_object(obj) {
	ret_string="";
	task = obj["task"];
	ret_string="<b>Description</b>:"+task["@description"]+"</br>";
	ret_string+="<b>Difficulty</b>:"+task["@difficulty"]+"</br>";
	if("tag" in task){
		ret_string+="<b>Tags</b>:";
		tags = task["tag"];
		ret_string += tags.join(", ")+"</br>"
	}
	console.log(ret_string);
	if("testcases" in task){
		ret_string+="<b>Testcases</b>:";
		testcases = task["testcases"]["testcase"];
		for(testcase in testcases){
			if(typeof(testcase['arg']) == ''){
			ret_string+="args: ("+ testcase["arg"].join(", ");
			//", outcome: "+ testcase['outcome'];
			}
		}
	}
  	return ret_string;
}