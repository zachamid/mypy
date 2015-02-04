#!/usr/bin/python

import cgi,cgitb,json,os,datetime,MySQLdb,db_connection
import task_correction, task_delivery
cgitb.enable()

print '''Content-type: text/html\n\n

<html>
<body>
'''
f=open("unit_test_files/code1.py",'r')
code1= f.read()
f=open("unit_test_files/code2.py",'r')
code2= f.read()
f=open("unit_test_files/code3.py",'r')
code3= f.read()
f=open("unit_test_files/code4.py",'r')
code4= f.read()

print '<pre>'+code1+'</pre>'
print '<pre>'+code2+'</pre>'
print '<pre>'+code3+'</pre>'
print '<pre>'+code4+'</pre>'

print '<pre>'
print task_correction.teachers_report(code1,code1)
print '</pre></br></br><pre>'
print task_correction.teachers_report(code1,code2)
print '</pre></br></br><pre>'
print task_correction.teachers_report(code2,code3)
print '</pre></br></br><pre>'
print task_correction.teachers_report(code3,code2)
print '</pre></br></br>'

print '</body></html>'