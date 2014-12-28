function run_code(code,output,err) {
   	var mypre = document.getElementById(output);
   	var error_area = document.getElementById(err);
   	mypre.value = '';
   	error_area.value = '';
   	var outf = function(text){
   		var mypre = document.getElementById(output);
   		mypre.value = mypre.value + text;
   	};
   	Sk.configure({output:outf});
   	try {
    	eval(Sk.importMainWithBody("<stdin>",false,code));
   	} catch (e) {
   		error_area.value = e;
   	}
}

function compile_code(code, task_id, output, err){
	$.ajax({
		url : '/read_task_information.py',
    	data: {cmd:"Get_Task_Compile_Code",task_id:task_id, code: code},
    	type: 'POST',
    	dataType: 'json'}).done(function(code){
    		run_code(code['code'],output, err);
    });
}

function auto_generate(struct, text_area){
	text_area_DOM = document.getElementById(text_area);
	cursor_start = text_area_DOM.selectionStart;
	cursor_end = text_area_DOM.selectionEnd;
	text = text_area_DOM.value;
	text_before = text.substring(0, cursor_start);
	text_after = text.substring(cursor_end, text.length);
	code = '';
	switch(struct){
		case 'for':
			code = 'for i in xrange(start,finish):\n\t#Code to be iterated';
			break;
		case 'while':
			code = 'while(condition):\n\t #Code to be iterated';
			break;
		case 'if':
			code = 'if(condition):\n\t #Code to be executed';
			break;
	}
	text_area_DOM.value = text_before+code+text_after;
}

function code_area_prep(){
	BehaveHooks.add(['keydown'], function(data){
				var numLines = data.lines.total,
					house = document.getElementsByClassName('line-nums')[0],
					html = '',
					i;
				for(i=0; i<numLines; i++){
					html += '<div>'+(i+1)+'</div>';
				}
				house.innerHTML = html;
			});
	BehaveHooks.add(['keydown'], function(data){
				var numLines = data.lines.total,
					fontSize = parseInt( getComputedStyle(data.editor.element)['font-size'] ),
					padding = parseInt( getComputedStyle(data.editor.element)['padding'] );
					if(parseInt(data.editor.element.style.height) > ((numLines*fontSize)+padding) ) {
						data.editor.element.style.height = (((numLines*fontSize)+padding))+'px';
					}
		});
}