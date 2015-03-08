#!/usr/bin/python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components, db_connection
from task_correction import calc_score as calc_score
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()
type = ''
html_header = ''
name = ''
students = {}
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)+'\n'
	if cookies['type'].value == 'Student':
		html_header += 'Location:../index.py'
	else:
		if 'id' in cookies:
			cursor = db_connection.get_connection()
			sql = '''SELECT FirstName, LastName, Administrator
					FROM Teacher 
					WHERE TeacherID='''+str(cookies['id'].value)
			cursor.execute(sql)
			teacher_info = cursor.fetchone()
			name = teacher_info['FirstName']+' '+teacher_info['LastName']
			
			if teacher_info['Administrator']:
				type = 'Administrator'
			else:
				type = 'Teacher'


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
			students = []
			for student in student_info:
				student_stats={}
				student_stats['id'] = student['StudentID']
				student_stats['name'] = student['FirstName']+' '+student['LastName']
				sql = '''SELECT ProgressID, Correctness_Points, Similarity_Points,
						Attempts_Points, Time_Points
						FROM Progress WHERE StudentID=%d ''' % (student['StudentID'])
				cursor.execute(sql)
				progress_info = cursor.fetchall()
				student_stats['no_tasks'] = cursor.rowcount;
				running_total = 0
				for progress in progress_info:
					running_total += calc_score(progress['Correctness_Points'],progress['Similarity_Points'],progress['Attempts_Points'],progress['Time_Points'])
				if(student_stats['no_tasks'] == 0):
					student_stats['avg_score'] = 0
				else:
					student_stats['avg_score'] = (float)(running_total)/student_stats['no_tasks']
				students.append(student_stats)
else:
	html_header +=  'Location: index.py'


include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('class_results_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, type=type, name=name, students=students)