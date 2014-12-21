function check_directory(data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Get_Task_File_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(result){
    		data_manipulation(result);
    	});
}
    		
function get_task_info(taskID,data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Get_Task_Info",params:taskID},
    	type: 'POST',
    	dataType: 'text'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_info(data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Get_Task_DB_Info"},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_xml(task_id, data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Get_Task_XML_Info", params:task_id},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function get_task_py(task_id, file_name, data_manipulation){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Get_Task_Python_File", params:task_id, params_2:file_name},
    	type: 'POST',
    	dataType: 'json'}).done(function(tasks){
    			data_manipulation(tasks);
    });
}

function print_xml_object(obj) {
	ret_string="";
	if "task" in obj{
		task = obj["task"];
		ret_string="<b>Description</b>:"+task["@description"]+"</br>";
		ret_string+="<b>Difficulty</b>:"+task["@difficulty"]+"</br>";
		if("tag" in task){
			ret_string+="<b>Tags</b>:";
			tags = task["tag"];
			if(Array.isArray(tags)){
				ret_string += tags.join(", ");
			}
			else{
				ret_string += tags;
			}
			ret_string += "</br>";
		}
		if("testcase" in task){
			ret_string+="<b>Testcases</b>:";
			testcases = task['testcase'];
			if(Array.isArray(testcases)){
				for(testcase in testcases){
					if(Array.isArray(testcase['arg'])){
						ret_string+="args: ("+ testcases[testcase]["arg"].join(", ")+")";
						}
					else{
						ret_string+="args: ("+ testcases[testcase]["arg"] + ")";
					}
					ret_string += ", outcome: "+ testcases[testcase]['out']+"</br>";
				}
			}
			else{
				if(Array.isArray(testcases['arg'])){
					ret_string+="args: ("+ testcases["arg"].join(", ")+")";
				}
				else{
					ret_string+="args: ("+ testcases["arg"] + ")";
				}
				ret_string += ", outcome: "+ testcases['out']+"</br>";
			}
		}
	}
	else{
		for (var key in obj) {
    		if (typeof(obj[key]) == 'object') {
      			ret_string+=print_object(obj[key])+"</br>";
    		} else {
    			ret_string+="<b>" + key + "</b>: " + obj[key]+"</br>";
    		}
    	}
  	}
  	return ret_string;