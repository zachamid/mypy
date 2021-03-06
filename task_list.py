#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os, task_delivery
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

html_header = ''
tasks = []
name = ''
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	cursor = db_connection.get_connection()
	cursor.execute('SELECT FirstName, LastName FROM %s WHERE %sID=%s' % (cookies['type'].value,cookies['type'].value,str(cookies['id'].value)))
	record = cursor.fetchone()
	name = record['FirstName']+' '+record['LastName']
	file_info = task_delivery.get_file_info()
	counter = 0
	for task in file_info:
		if(file_info[task]['directory'] == 1 
		and file_info[task]['task_complete.py'] == 1
		and file_info[task]['task_skeleton.py'] == 1 
		and file_info[task]['info.xml'] == 1):
			new_task= {}
			cursor.execute('SELECT * FROM Task WHERE TaskID='+str(task))
			task_xml = task_delivery.get_task_xml(task)
			new_task = cursor.fetchone()
			new_task.update(task_xml['task'])
			cursor.execute('''SELECT DateStarted, DateModified, DateCompleted 
							FROM Progress 
							WHERE TaskID='''+str(task)+' AND StudentID='+str(cookies['id'].value))
			counter=counter+1
			progress_info = cursor.fetchone()
			new_task['Dates'] = progress_info
			
			tasks.append(new_task)
else:
	html_header += 'Location:index.py'			


include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('task_list_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, tasks=tasks, type=type)