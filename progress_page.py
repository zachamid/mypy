#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
from task_correction import calc_score as calc_score
from mako.template import Template
from mako.lookup import TemplateLookup
cgitb.enable()

html_header = ''
name = ''
progress_records = ()
score = {}
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	cursor = db_connection.get_connection()
	cursor.execute('SELECT FirstName, LastName FROM Student WHERE StudentID='+cookies['id'].value)
	names = cursor.fetchone()
	name = names['FirstName']+' '+names['LastName']
	cursor.execute('''SELECT * FROM Progress
					INNER JOIN Task
					ON Progress.TaskID = Task.TaskID
					WHERE Progress.StudentID=%s'''%(cookies['id'].value))
	progress_records = cursor.fetchall()
	for record in progress_records:
		score[record['TaskID']] = calc_score(record['Correctness_Points'],record['Similarity_Points'],record['Attempts_Points'],record['Time_Points'])
	
	if cookies['type'].value == 'Teacher':
		html_header += 'Location: index.py'
else:
	html_header += 'Location: index.py'
	
include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('progress_page_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, progress_records=progress_records, score=score)