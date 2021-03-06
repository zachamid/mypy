#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os,datetime,re
import task_delivery, task_correction
cgitb.enable()
from mako.template import Template
from mako.lookup import TemplateLookup

name = ''
html_header = ''
cursor = db_connection.get_connection()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
task_info = cgi.FieldStorage()
task_id = task_info['task_id'].value

correct_output = task_delivery.get_python_code_from_file(task_id, 'result.txt')['result.txt']
correct_code = task_delivery.get_python_code_from_file(task_id, 'task_complete.py')['task_complete.py']

submitted_code = ''
submitted_output = ''
correctness_score = 0
jaccard_score = 0
attempt_score = 0
time_score = 0
if cookies.has_key('id') and cookies.has_key('type') and task_info.has_key('task_id'):
	if cookies['type'] == 'Teacher':
		html_header += 'Location: index.py'
	else:
		html_header += str(cookies)
		cursor.execute('SELECT FirstName, LastName FROM Student WHERE StudentID='+cookies['id'].value)
		record=cursor.fetchone()
		name = record['FirstName']+' '+record['LastName']
		if cookies['type'].value == 'Student':
			student_id = cookies['id'].value
			task_id = task_info['task_id'].value
			currtime = datetime.datetime.now()
			if('code' in task_info):
				sql = '''UPDATE Progress SET DateCompleted='%s'
						WHERE StudentID=%s 
			 			AND TaskID=%s''' % (str(currtime),str(student_id),str(task_id))
				cursor.execute(sql)
		
				submitted_code = task_info['code'].value.replace('\r\n','\n')
				submitted_code = submitted_code.replace('&nbsp;&nbsp;&nbsp;&nbsp;','\t').rstrip()
		
				submitted_output = task_info["output"].value.replace('\r\n','\n')
				
				sql = '''SELECT DateStarted, DateCompleted,Attempts FROM Progress WHERE StudentID=%s AND TaskID=%s
				''' % (str(student_id),str(task_id))
				cursor.execute(sql)
				progress_record = cursor.fetchone()
		
				sql = '''SELECT ProgressID, DateStarted, DateCompleted FROM Progress WHERE TaskID=%s
						''' % (str(task_id))
				cursor.execute(sql)
				times = cursor.fetchall()
	
				correctness_score = task_correction.judge_correctness(correct_output,submitted_output)
		
				jaccard_score = task_correction.compare_asts(correct_code, submitted_code)
			
				attempt_score = task_correction.judge_attempts(progress_record['Attempts'])
	
				min_time = task_correction.quickest_time(times)
				task_correction.remark_time(min_time, times)
				task_time = (progress_record['DateCompleted']-progress_record['DateStarted']).seconds
				time_score = task_correction.judge_time(min_time, task_time)
			
				sql = 'UPDATE Progress SET Correctness_Points='+str(correctness_score)+',Similarity_Points='+str(jaccard_score)
				sql +=', Time_Points='+str(time_score)+', Output=\''+submitted_output.replace('\'','\\\'')+'\', Code=\''+submitted_code.replace('\'','\\\'')+'\', Attempts_Points='+str(attempt_score)
				sql +=' WHERE StudentID='+str(student_id)+' AND TaskID='+str(task_id)
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
else:
	html_header += 'Location: index.py'
	
	
total_score = task_correction.calc_score(correctness_score, jaccard_score, time_score, attempt_score)
code_report=task_correction.teachers_report(submitted_code, correct_code)
output_report=task_correction.teachers_report(submitted_output, correct_output)

scores={'correctness': correctness_score, 'similarity': jaccard_score, 'time': time_score, 'attempts': attempt_score, 'total_score':total_score}
submission={'code': code_report, 'output': output_report}
include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('correction_page_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, submission=submission, scores=scores)