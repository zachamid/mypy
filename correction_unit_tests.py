#!/usr/bin/python

import cgi,cgitb,json,os,datetime,MySQLdb,db_connection
import task_correction, task_delivery
cgitb.enable()

print '''Content-type: text/html\n\n

<html>
<head>
<style>
	table,td,th, tr {
    	border: 1px solid black;
		width: 50%
	}
</style>
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

print '<table><tr><th>Entrant 1</th><th>Entrant 2</th><th>Entrant 3</th><th>Entrant 4</th>'
print '</tr><tr><td><pre>'+code1+'</pre></td>'
print '<td><pre>'+code2+'</pre></td>'
print '<td><pre>'+code3+'</pre></td>'
print '<td><pre>'+code4+'</pre></td>'
print '</tr></table></br></br>'


print '<table><tr><th></th><th>Teachers Report</th><th>Compare ASTs</th></tr>'
for i in (code1,code2,code3,code4):
	for j in (code1,code2,code3,code4):
		print '<tr><td><pre>'
		task_correction.teachers_report(i,j)
		print '</pre></td><td><pre>'
		task_correction.compare_asts(i,j)
		print '</pre></td></tr>'
print '</table>'
print '</body></html>'