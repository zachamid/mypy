function run_code(code_area,output,err) {
   	var code = document.getElementById(code_area).value;
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

function auto_generate(struct){
	switch(struct){
		case 'for':
		case 'While':
		
	}
}