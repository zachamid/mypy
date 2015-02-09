#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os,datetime,re
import task_delivery, task_correction
cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	if cookies['type'] == 'Teacher':
		print 'Location: index.py'
	else:
		print cookies
else:
	print 'Location: index.py'

task_info = cgi.FieldStorage()
student_id = cookies['id'].value
task_id = task_info['task_id'].value
code = task_info['code'].value
codetocorrect = re.sub("\n\n", "\n", code).replace('</br>','\n')
codetocorrect = codetocorrect.replace('&nbsp;&nbsp;&nbsp;&nbsp;','\t').rstrip()
output = task_info["output"].value
cursor = db_connection.get_connection()
task_delivery.save_code(codetocorrect, task_id, student_id)

print """Content-type: text/html\n\n

<html>
	<head>
		<script src="skulpt-latest/skulpt.min.js" type="text/javascript"></script> 
		<script src="skulpt-latest/skulpt-stdlib.js" type="text/javascript"></script> 
		<script src="jquery-1.11.1.min.js" type="text/javascript"></script> 
		<script src="behave.js" type="text/javascript"></script>
		<script src="python_functions.js" type="text/javascript"></script>
		<script src="user_functions.js" type="text/javascript"></script>
		<script src="task_admin_functions.js" type="text/javascript"></script>
		<link rel="stylesheet" type="text/css" href="general_style.css">
    	<link rel="stylesheet" type="text/css" href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
    	<style>
			table,td,th, tr {
    			border: 1px solid black;
    			padding: 10px;
			}
			
		</style>
    </head>
	<body>
"""
common_components.print_navbar(cookies['id'].value,'')
outputtocorrect = output.replace('</br>','\n').replace('&nbsp;&nbsp;&nbsp;&nbsp;','\t')
print """&nbsp
		<div class="container">
      		<div class="panel panel-default">
      			<table style="width:100%">
      				<tr>
      					<td>
      					<div class='container' style="width:100%">
							<textarea rows="10" readonly style="overflow:auto;resize:none">
"""
print codetocorrect
print """&nbsp				</textarea></div></div>
						</td>
						<td>
      					<div class='container' style="width:100%">
							<textarea rows="10" readonly style="overflow:auto;resize:none">
"""
print outputtocorrect
print """&nbsp				</textarea></div></div>
						</td>
					</tr>
					<tr>
						<td>
							Correctness
						</td>
						<td>
"""
correct_output = correctcode = task_delivery.get_python_code_from_file(task_id, 'result.txt')['result.txt']
print task_correction.judge_correctness(correct_output,outputtocorrect)
print """&nbsp 			</td>
					</tr>
					<tr>
						<td>
							Similarity to Model Answer
						</td>
						<td>"""
#print task_correction.judge_similarity(task_id, codetocorrect)
print "<pre>"
correctcode = task_delivery.get_python_code_from_file(task_id, 'task_complete.py')['task_complete.py']
jaccard_score = task_correction.compare_asts(correctcode, codetocorrect)
correctcode = re.sub("\n\n", "\n", correctcode)
correctcode = re.sub(' +','  ',correctcode).split('\n')
codetocorrect = re.sub(' +','  ',codetocorrect).split('\n')
task_correction.printDiff(task_correction.longest_common_subsequence(codetocorrect,correctcode), codetocorrect, correctcode, len(codetocorrect), len(correctcode))
print "				</pre></br>"
print jaccard_score
print """\n
						</td>
					</tr>
					<tr>
						<td>
							Time
						</td>
						<td>
"""
#task_correction.judge_time(task_id,codetocorrect)
print """&nbsp			</td>
					</tr>
					<tr>
						<td>
							Attempts
						</td>
						<td>"""
#task_correction.judge_attempts(task_id, codetocorrect)
print """&nbsp			</td>
					</tr>
				</table>
"""

print """\n
		</div></div>
	</body>
</html>
"""