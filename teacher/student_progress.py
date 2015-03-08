#!/usr/bin/python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import db_connection, task_correction
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cursor = db_connection.get_connection()
student_id = cgi.FieldStorage()['studentID'].value

cursor.execute('''SELECT * FROM Progress
				LEFT JOIN Task
				ON Task.TaskID = Progress.TaskID
				WHERE Progress.StudentID ='''+str(student_id))
attempts = cursor.fetchall()
for attempt in attempts:
	attempt['Score'] = calc_score(attempt['Correctness_Points'],attempt['Similarity_Points'],attempt['Time_Points'],attempt['Attempts_Points'])
template_file = open('student_progress_template.html')
page_template = Template(template_file.read())
print page_template.render(attempts=attempts)