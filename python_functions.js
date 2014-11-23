function run_code(code,output) {
   	var prog = document.getElementById(code).value;
   	var mypre = document.getElementById(output);
   	mypre.innerHTML = '';
   	var outf = function(text){
   		var mypre = document.getElementById(output);
   		mypre.value = mypre.value + text;
   	};
   	Sk.configure({output:outf});
   	try {
    	eval(Sk.importMainWithBody("<stdin>",false,prog));
   	} catch (e) {
   		alert(e);
   	}
}