function read_task_information(cmd, params, post_function){
	var data = {cmd: cmd};
  	for(key in params){
  		data[key]=params[key];
  	}
    $.ajax({
    	data : data,
    	url : '/read_task_information.py',
    	type : "POST",
    	dataType : "json"}).done(function(result){
    		post_function(result);
    	});
}

function print_xml_object(obj) {
	ret_string="";
	if("task" in obj){
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
}