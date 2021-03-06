#!/usr/bin/python

import sys, getopt
import getpass
import importlib
import distutils

# Importing all relevant python modules
required_mods = ['cgi','cgitb','json','MySQLdb','os','datetime','re','mako',
	'hashlib','operator','xml','xmltodict','pylev','math','ast','sys']

flag = 0
for mod in required_mods:
	try:
		importlib.import_module(mod)
	except ImportError,e:
		flag = 1
		print 'Please install ',mod,' to ensure system runs properly'

if flag == 1:
	print 'Script halting'			

# retrieve database information
# Store input and output file names
host=''
username=''
table=''
tasks_path = '../../'
 
# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"h:u:t:p:",['host=','username=','table=','tasks_path='])
 
###############################
# o == option
# a == argument passed to the o
###############################
for opt, arg in myopts:
    if opt in ('-h','--host'):
        host = arg
    elif opt in ('-u','--username'):
        username = arg
    elif opt in ('-t','--table'):
    	table = arg
    elif opt in ('-p', '--tasks_path'):
    	tasks_path = ''
    else:
        print("Usage: %s -h host -u username -t table" % sys.argv[0])

password = getpass.getpass('Enter the password for '+username+'@'+host)

# connect to database
importlib.import_module('MySQLdb')
importlib.import_module('MySQLdb.cursors')
importlib.import_module('mako.template')
importlib.import_module('mako.lookup')
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