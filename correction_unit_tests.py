#!/usr/bin/python

import cgi,cgitb,json,os,datetime,MySQLdb,db_connection
import task_correction, task_delivery
cgitb.enable()

print '''Content-type: text/html\n\n

<html>
<body>
<h1>Correction Unit Tests</h1></br>
'''
f=open("unit_test_files/code1.py",'r')
code1= f.read()
f=open("unit_test_files/code2.py",'r')
code2= f.read()
f=open("unit_test_files/code3.py",'r')
code3= f.read()
f=open("unit_test_files/code4.py",'r')
code4= f.read()

print '<h2>Model Answer</h2><br><pre>'+code1+'</pre>'

print '<table width="100%"><tr><th>Entrant 1</th><th>Entrant 2</th>'
print '</tr><tr><td><pre>'+code1+'</pre></td>'
print '<td><pre>'+code2+'</pre></td></tr>'
print '<tr><th>Entrant 3</th><th>Entrant 4</th></tr>'
print '<td><pre>'+code3+'</pre></td>'
print '<td><pre>'+code4+'</pre></td>'
print '</tr></table>'


print '<pre>'
task_correction.teachers_report(code1,code1)
print '</pre></br></br><pre>'
task_correction.teachers_report(code1,code2)
print '</pre></br></br><pre>'
task_correction.teachers_report(code2,code3)
print '</pre></br></br><pre>'
task_correction.teachers_report(code3,code2)
print '</pre></br></br>'

print '</body></html>'