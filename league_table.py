#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
from operator import itemgetter, attrgetter
from  task_correction import calc_score as calc_score
from mako.template import Template
from mako.lookup import TemplateLookup
cgitb.enable()

html_header = ''
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	if cookies['type'].value == 'Teacher':
		html_header += 'Location: index.py'
else:
	html_header += 'Location: index.py'

league_entry = []
name = ''
league_order = []
if cookies['type'].value == 'Student':
	cursor = db_connection.get_connection()
	cursor.execute('''SELECT FirstName, LastName, ClassID FROM Student WHERE StudentID=%s''' % (cookies['id'].value))
	student_record = cursor.fetchone()
	name = student_record['FirstName'] + ' ' + student_record['LastName']
	cursor.execute('''SELECT StudentID, FirstName, LastName FROM Student
					WHERE ClassID=%s''' % (student_record['ClassID']))
	class_list = cursor.fetchall()

	for student in class_list:
		new_entry = {}
		new_entry['student'] = str(student['StudentID'])
		new_entry['total_score'] = 0
		cursor.execute('''SELECT Correctness_Points,Similarity_Points, Attempts_Points, Time_Points 
							FROM Progress WHERE StudentID='''+str(student['StudentID']))
		progress_records = cursor.fetchall()
		for record in progress_records:
			score = calc_score(record['Correctness_Points'],record['Similarity_Points'],record['Attempts_Points'],record['Time_Points'])
			new_entry['total_score'] += score
		new_entry['no_tasks'] = len(progress_records)
		new_entry['name']= student['FirstName']+' '+student['LastName']
		league_entry.append(new_entry)
		
	league_order=sorted(league_entry, key=lambda e: e['total_score'], reverse=True)

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('league_table_template.html','r')

template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, league_order=league_order)