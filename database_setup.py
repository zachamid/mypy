#!/usr/bin/python

import MySQLdb
import sys
import getopt

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hs:d:u:p",["server=","database=","username=","password="])
	except getopt.GetoptError:
		print 'database_setup.py -s <server_url> -d <database_name> -username <username> -password <password>'
		sys.exit(2)
	serverName = '';
	databaseName = '';
	userName = '';
	passWord = '';
	for opt, arg in opts:	
		if opt == '-h':
        	print 'database_setup.py -s <server_url> -d <database_name> -username <username> -password <password>'
        	sys.exit()
        elif opt == '-s':
        	serverName = arg
        elif opt == '-d':
        	databaseName = arg
        elif opt == '-u':
        	userName = arg
        elif opt == '-p':
        	passWord = arg
    db = MySQLdb.connect(serverName,userName,passWord,databaseName);
    cursor = db.cursor()
    sql = """CREATE TABLE Student(
    		FirstName CHAR(20)
    		LastName CHAR(20)
    		ClassID INT
    		
    		)"""
    cursor.execute()