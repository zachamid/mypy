#!/usr/bin/python

import sys, getopt
import MySQLdb, MySQLdb.cursors
import getpass
import importlib
import distutils
from mako.template import Template
from mako.lookup import TemplateLookup

# Importing all relevant python modules
required_mods = ['cgi','cgitb','json','MySQLdb','Cookie','os','datetime','re','mako',
	'hashlib','operator','xml','xmltodict','pylev','math','ast','sys']

for mod in required_mods:
	try:
		importlib.import_module(mod)
	except ImportError:
		distutils.core.setup(mod)
			

# retrieve database information
opts, args = getopt.getopt(sys.argv[:1],"o:v:",["host=","username=","table=","tasks_dir="]);

host = ''
user = ''
db = ''
tasks_path = ''

for opt, arg in options:
    if opt in ('-h', '--host'):
        host = arg
    elif opt in ('-u', '--username'):
        username = arg
    elif opt in ('-t','--table'):
        db = arg
    elif opt in ('-d','--task_dir'):
    	tasks_path = arg

password = getpass.getpass('Enter the password for '+username+'@%'+host)

# connect to database
try:
	connection = MySQLdb.connect(host,user,password,table, cursorclass=MySQLdb.cursors.DictCursor)
	cursor = connection.cursor()
	db_setup = open('database_setup.sql','r').read().split(';\n')
	for query in db_setup:
		cursor.execute(query)
except MySQLdb.Error, e:
	try:
		print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
	except IndexError, e:
		print "MySQL Error: %s" % str(e)


# rewrite db_connection file
connection_file = open('db_connection.py','w+')
content = '''
#!/usr/bin/python

import MySQLdb
import MySQLdb.cursors

def get_connection():
	db = MySQLdb.connect('%s','%s','%s','%s', cursorclass=MySQLdb.cursors.DictCursor)
	cursor = db.cursor()
	return cursor
''' % (host,user,password,db)
connection_file.write(content)
connection_file.close()

# create tasks directory
try:
	mkdir(tasks_path+'/tasks')
except os.error, e:
	try:
		print 'OS Error [%d]: %s ' % (e.args[0], e.args[1])
	except:
		print 'OS Error: %s' % str(e)
task_delivery_file=open('task_delivery.py','w+')
task_delivery_template=open('task_delivery.py','r').read()
page_template = Template(task_delivery_template)
task_delivery_file.write(page_template.render(tasks_path=tasks_paths))
task_delivery_file.close()