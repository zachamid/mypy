#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
cgitb.enable()

posted_data = cgi.FieldStorage()
cmd = posted_data['cmd'].value
cursor = db_connection.get_connection()
sql_query=''
if(cmd == 'Classes'):
	sql_query = "SELECT * FROM Class"
elif(cmd == 'Progress'):
	student_id = posted_data['StudentID'].value
	sql_query = "SELECT * FROM Progress WHERE StudentID='"+str(student_id)+"'"
elif(cmd == 'CheckEmail'):
	email = posted_data['Email'].value
	sql_query = "SELECT Email FROM Student WHERE Email='"+email+"' UNION "
	sql_query = sql_query+"SELECT Email FROM Teacher WHERE Email='"+email+"'"
elif(cmd == 'ClassList'):
	classID = posted_data['ClassID'].value
	sql_query = "SELECT * FROM Student WHERE ClassID="+classID
elif(cmd == 'Teachers'):
	sql_query = 'SELECT TeacherID, FirstName, LastName FROM Teacher'
elif(cmd == 'ClassTeacherList'):
	sql_query = """
		SELECT Class.ClassID, Class.ClassName, Teacher.TeacherID, Teacher.FirstName, TeacherClassRelationship.TeacherClassRelID,
		Teacher.LastName
		FROM Class
		INNER JOIN TeacherClassRelationship
		ON Class.ClassID = TeacherClassRelationship.ClassID
		INNER JOIN Teacher
		ON Teacher.TeacherID = TeacherClassRelationship.TeacherID
		ORDER BY Class.ClassID ASC
	"""
elif(cmd == 'Admins'):
	sql_query = 'SELECT TeacherID, FirstName, LastName FROM Teacher WHERE Administrator='+posted_data['AdminFlag'].value
	

cursor.execute(sql_query)
data = cursor.fetchall() 
print """content-type: text/html

"""
print json.dumps(data)

