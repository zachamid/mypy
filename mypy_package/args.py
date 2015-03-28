#!/usr/bin/python
import sys, getopt, getpass

# Store input and output file names
host=''
username=''
table=''
 
# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"h:u:t:",['host=','username=','table='])
 
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
    else:
        print("Usage: %s -h host -u username -t table" % sys.argv[0])
 
# Display input and output file name passed as the args
password = getpass.getpass('Enter the password for '+username+'@'+host)

print "Host: %s, Username: %s, Password: %s, Table: %s" % (host,username,password,table)