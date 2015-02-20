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
		ret_string="<b>Description</b>:"+task["description"]['#text']+"</br>";
		ret_string+="<b>Intructions</b>:"+task["instruction"]['#text']+"</br>";
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
			if(testcases['@type'] == 'list'){
				testcases = testcases['item']
				for(var index=0; index<testcases.length; index++){
					ret_string += "description"+ testcases[index]['description']['#text']+",";
					ret_string+="args: ("+ testcases['testcase']["arg"]['#text'] + ")</br>";
				}
			}
			else{
				
				ret_string += "description"+ testcases['testcase']['description']['#text']+",";
				ret_string+="args: ("+ testcases['testcase']["arg"]['#text'] + ")</br>";
			}
		}
	}
  	return ret_string;
}