#!/usr/bin/python -w

import cgi
import cgitb;
cgitb.enable()


try:
    db = MySQLdb.connect('localhost','root','S0crat3s34!','test');

    cursor = db.cursor()
    cursor.execute("SELECT * FROM Student")

    ver = cursor.fetchall()
    
    for line in ver:
	    print line
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if db:    
        db.close()