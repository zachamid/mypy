#!/usr/bin/python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import db_connection, task_correction
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cursor = db_connection.get_connection()
student_id = cgi.FieldStorage()['StudentID'].value

cursor.execute('''SELECT * FROM Progress
				LEFT JOIN Task
				ON Task.TaskID = Progress.TaskID
				WHERE Progress.StudentID ='''+str(student_id))
attempts = cursor.fetchall()

template_file = open('student_progress_template.html')
page_template = Template(template_file.read(), lookup=include_lookup)
print page_template.render(attempts=attempts)