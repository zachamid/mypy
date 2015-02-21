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
cursor = db_connection.get_connection()

task_info = cgi.FieldStorage()
student_id = cookies['id'].value
task_id = task_info['task_id'].value
currtime = datetime.datetime.now()
if('code' in task_info):
	sql = '''UPDATE Progress SET DateCompleted='%s'
			 WHERE StudentID=%s AND TaskID=%s''' % (str(currtime),str(student_id),str(task_id))
	cursor.execute(sql)
	correct_output = correctcode = task_delivery.get_python_code_from_file(task_id, 'result.txt')['result.txt']
	correct_code = task_delivery.get_python_code_from_file(task_id, 'task_complete.py')['task_complete.py']
	
	submitted_code = task_info['code'].value
	submitted_code = submitted_code.replace('</br>','\n')
	submitted_code = submitted_code.replace('&nbsp;&nbsp;&nbsp;&nbsp;','\t').rstrip()
	
	submitted_output = task_info["output"].value
	submitted_output = submitted_output.replace('</br>','\n').replace('&nbsp;&nbsp;&nbsp;&nbsp;','\t')
	
	sql = '''SELECT DateStarted, DateCompleted,Attempts FROM Progress WHERE StudentID=%s AND TaskID=%s
			''' % (str(student_id),str(task_id))
	cursor.execute(sql)
	progress_record = cursor.fetchone()
	
	sql = '''SELECT DateStarted, DateCompleted FROM Progress WHERE TaskID=%s
			''' % (str(task_id))
	cursor.execute(sql)
	times = cursor.fetchall()
	
	correctness_score = task_correction.judge_correctness(correct_output,submitted_output)
	
	jaccard_score = task_correction.compare_asts(correct_code, submitted_code)
	
	attempt_score = task_correction.judge_attempts(progress_record['Attempts']+1)
	
	min_time = task_correction.quickest_time(times)
	task_time = (progress_record['DateCompleted']-progress_record['DateStarted']).seconds
	time_score = task_correction.judge_time(min_time, task_time)
	
	sql = 'UPDATE Progress SET Correctness_Points='+correctness_score+',Similarity_Points='+jaccard_score
	sql +=', Time_Points='+time_score+', Attempts_Points='+attempt_score+', Output='+submitted_output+', Code='+submitted_code+', Attempts='+(progress_record['Attempts']+1)
	sql +=' WHERE StudentID='+str(student_id)+' AND TaskID='+str(task_id))
	cursor.execute(sql)

else:
	sql = '''SELECT * FROM Progress WHERE StudentID=%s AND TaskID=%s''' % (str(student_id),str(task_id))
	cursor.execute(sql)
	progress_record = cursor.fetchone()

	submitted_code = progress_record['Code']
	submitted_output = progress_record['Output']
	
	correctness_score = progress_record['Correctness_Points']
	jaccard_score = progress_record['Similarity_Points']
	attempt_score = progress_record['Attempts_Points']
	time_score = progress_record['Time_Points']


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
print """&nbsp
		<div class="container">
      		<div class="panel panel-default">
      			<table style="width:100%">
      				<tr>
      					<td>
      					<div class='container' style="width:100%">
							<textarea rows="10" readonly style="overflow:auto;resize:none">
"""
print submitted_code
print """&nbsp				</textarea></div></div>
						</td>
						<td>
      					<div class='container' style="width:100%">
							<textarea rows="10" readonly style="overflow:auto;resize:none">
"""
print submitted_output
print """&nbsp				</textarea></div></div>
						</td>
					</tr>
					<tr>
						<td>
							Correctness
						</td>
						<td>
"""
print correctness_score
print """&nbsp 			</td>
					</tr>
					<tr>
						<td>
							Similarity to Model Answer
						</td>
						<td>"""
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
print time_score
print """&nbsp			</td>
					</tr>
					<tr>
						<td>
							Attempts
						</td>
						<td>"""
print attempt_score
print """&nbsp			</td>
					</tr>
					<tr>
						<td>
							<b> Total Score</b>
						</td>
						<td><b>
"""
print task_correction.calc_score(correctness_score, jaccard_score, time_score, attempt_score)
"""\n
						</b></td>
					</tr>
				</table>
"""

print """\n
		</div></div>
	</body>
</html>
"""
