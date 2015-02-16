#!/usr/bin/env python

import cgi, cgitb, os,sys
sys.path.append(os.pardir)
import db_connection, task_correction, task_delivery

cursor = db_connection.get_connection()
attempt_info = cgi.FieldStorage()
student_id = attempt_info['id'].value
task_id = attempt_info['task_id'].value
sql_query = 'SELECT * FROM Progress WHERE StudentID=%d AND TaskID=%d' % (student_id, task_id)
cursor.execute(sql_query)
progress_info = cursor.fetchone()

submitted_code = progress_info['Code']
submitted_output = progress_info['Output']

start_time = progress_info['DateStarted']
end_time = progress_info['DateCompleted']
correctness_score = progress_info['Correctness_Points']
jaccard_score = progress_info['Similarity_Points']
attempt_score = progress_info['Attempts_Points']
attempts = progress_info['Attempts']
time_score = progress_info['Time_Points']

time_taken=end_time - start_time

correct_output = correctcode = task_delivery.get_python_code_from_file(task_id, 'result.txt')['result.txt']
correct_code = task_delivery.get_python_code_from_file(task_id, 'task_complete.py')['task_complete.py']

print """Content-type: text/html\n\n


"""
print '''\n
<table>
	<tr>
		<td><pre>
		'''
print task_correction.teachers_report(submitted_code, correct_code)
print '''\n
		</pre></td>
		<td><pre>'''
print task_correction.teachers_report(submitted_output, correct_output)	
print '''\n
		</td>
	</tr>
		<td colspan='2'>
		<b>Correctness</b>
		</td>
		<td colspan='2'>
			%u %
		</td>
	<tr>
		<td colspan='2'>
			<b>Similarity to Model Solution</b>
		</td>
		<td colspan='2'>
			%u %
		</td>
	</tr>
	<tr>
		<td>
			<b>Attempts</b>
		</td>
		<td>
			%d
		</td>
		<td>
			<b>Attempt Score</b>
		</td>
		<td>
			%u
		</td>
	</tr>
	<tr>
		<td>
			<b>Time</b>
		</td>
		<td>
			%s
		</td>
		<td>
			<b>Time Score</b>
		</td>
		<td>
			%u
		</td>
	</tr>
</table>
''' % (100*correctness_score, 100*similarity_score, attempts, 100*attempt_score,str(time_taken),100*time_score)