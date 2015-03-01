#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components, db_connection
from task_correction import calc_score as calc_score
from mako.template import Template

cgitb.enable()

html_header = ''
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += cookies
	if cookies['type'].value == 'Student':
		html_header += 'Location:../index.py'
else:
	html_header +=  'Location: index.py'

cursor = db_connection.get_connection()
sql = '''SELECT FirstName, LastName FROM Teacher WHERE TeacherID='''+str(cookies['id'].value)
cursor.execute(sql)
teacher_info = cursor.fetchone()
name = teacher_info['FirstName']+' '+teacher_info['LastName']


sql = '''SELECT TaskID from Task'''
cursor.execute(sql)
tasks = cursor.fetchall()

sql = '''SELECT Student.StudentID, Student.FirstName, Student.LastName FROM Student
		INNER JOIN TeacherClassRelationship
		ON Student.ClassID = TeacherClassRelationship.ClassID
		INNER JOIN Teacher
		ON Teacher.TeacherID = TeacherClassRelationship.ClassID
		WHERE TeacherClassRelationship.TeacherID=%s''' % (str(cookies['id'].value ))
cursor.execute(sql)
student_info = cursor.fetchall()
students = ()
counter = 0
for student in student_info:
	students[counter]={}
	students[counter]['name'] = student['FirstName']+' '+student['LastName']
	sql = '''SELECT ProgressID, Correctness_Points, Similarity_Points,
					Attempts_Points, Time_Points
				FROM Progress WHERE StudentID=%d ''' % (student['StudentID'])
	cursor.execute(sql)
	progress_info = cursor.fetchall()
	students[counter]['no_tasks'] = cursor.rowcount;
	running_total = 0
	for progress in progress_info:
		running_total += calc_score(progress['Correctness_Points'],progress['Similarity_Points'],progress['Attempts_Points'],progress['Time_Points'])
	if(students[counter]['no_tasks'] == 0):
		students[counter]['avg_score'] = 0
	else:
		students[counter]['avg_score'] = (float)(running_total)/students[counter]['no_tasks']
	counter++

mytemplate = Template(filename='class_results_template.html')
print(mytemplate.render(html_header=html_header, name=name, Students=students))