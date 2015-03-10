#!/usr/bin/env python

import cgi, cgitb, os,sys, Cookie
sys.path.append(os.pardir)
import db_connection, task_correction, task_delivery
from mako.template import Template
from mako.lookup import TemplateLookup

attempt_info = cgi.FieldStorage()
student_id = attempt_info['student_id'].value	
task_id = attempt_info['task_id'].value
name = ''
type = ''
html_header = ''
progress_info = {}
code_report = ''
output_report = ''
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type') and 'task_id' in attempt_info:
	html_header += str(cookies)
	if cookies['type'].value == 'Student':
		html_header += '\nLocation:../index.py\n'
	else:
		cursor = db_connection.get_connection()
		cursor.execute('''SELECT FirstName, LastName, Administrator FROM Teacher WHERE 
							TeacherID='''+str(cookies['id'].value))
		teacher_record = cursor.fetchone()
		name = teacher_record['FirstName'] + ' ' + teacher_record['LastName']
		type='teacher'
		if teacher_record['Administrator'] == 1:
			type = 'Administrator'
		
		sql_query = 'SELECT * FROM Progress WHERE StudentID=%s AND TaskID=%s' % (student_id, task_id)
		cursor.execute(sql_query)
		progress_info = cursor.fetchone()
	
		submitted_code = progress_info['Code']
		submitted_output = progress_info['Output']

		correct_output = task_delivery.get_python_code_from_file(task_id, 'result.txt')['result.txt']
		correct_code = task_delivery.get_python_code_from_file(task_id, 'task_complete.py')['task_complete.py']
		
		code_report = task_correction.teachers_report(submitted_code, correct_code)
		output_report = task_correction.teachers_report(submitted_output, correct_output)
		
		progress_info['total_score'] = task_correction.calc_score(progress_info['Correctness_Points'],progress_info['Similarity_Points'],progress_info['Attempts_Points'],progress_info['Time_Points'])
else:
	html_header += '\nLocation:index.py\n'
		
include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('attempt_info_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, type=type, name=name, scores=progress_info, code_report=code_report, output_report=output_report)