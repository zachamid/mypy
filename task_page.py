#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os,datetime
import task_delivery
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

html_header = ''
student_id = 0
task_id = 0
code = ''
task_xml = {}
name = ''
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
task_info = cgi.FieldStorage()

if task_info.has_key('task_id') and cookies.has_key('id') and cookies.has_key('type') :
	if cookies['type'] == 'Teacher':
		html_header += 'Location: index.py'
	else:
		html_header += str(cookies)
		task_id = task_info['task_id'].value
		student_id = cookies['id'].value
		cursor = db_connection.get_connection()
		cursor.execute('SELECT FirstName, LastName FROM %s WHERE %sID=%s' % (cookies['type'].value,cookies['type'].value,str(cookies['id'].value)))
		record = cursor.fetchone()
		name = record['FirstName']+' '+record['LastName']
		new_flag = 0
		curr_date = datetime.datetime.now()
		task_xml = task_delivery.get_task_xml(task_id)['task']	
		try:
			cursor.execute("""SELECT Attempts, ProgressID FROM Progress WHERE
						StudentID=%s AND TaskID=%s""" % (str(student_id),str(task_id)))

			if cursor.rowcount == 0:
				new_flag = 1
			else:
				progress_record = cursor.fetchone()
				cursor.execute("""UPDATE Progress SET DateModified=%s, 
								Attempts=%d WHERE ProgressID=%s"""% ("'"+str(curr_date)+"'", progress_record['Attempts']+1,progress_record['ProgressID']))
		except MySQLdb.Error, e:
			print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])

		if new_flag == 0:
			sql = '''SELECT Code FROM Progress
					 WHERE StudentID=%s AND TaskID=%s''' % (str(student_id),str(task_id))
			cursor.execute(sql)
			code = cursor.fetchone()['Code'].replace('</br>','\n')
		else:
			code = task_delivery.get_python_code_from_file(task_id, 'task_skeleton.py')['task_skeleton.py']
			cursor.execute("""INSERT INTO Progress (StudentID, TaskID, DateStarted, Code)
						Values('%s', '%s', '%s', '%s')""" % (str(student_id),str(task_id),str(curr_date),code.replace('\'','\\\'')))
else:
	html_header += 'Location: index.py'


include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('task_page_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, task_xml=task_xml, code=code, task_id = task_id, student_id=student_id)