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
  sql = """CREATE TABLE `Class` (
  		`ClassID` int(11) NOT NULL AUTO_INCREMENT,
  		`ClassName` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  		`School` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  		UNIQUE KEY `ClassID` (`ClassID`)
		)"""
  cursor.execute(sql)
  sql = """CREATE TABLE `Progress` (
  		`ProgressID` int(11) NOT NULL AUTO_INCREMENT,
  		`TaskID` int(11) NOT NULL,
  		`StudentID` int(11) NOT NULL,
  		`DateStarted` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  		`DateModified` timestamp NULL DEFAULT NULL,
  		`DateCompleted` timestamp NULL DEFAULT NULL,
  		`FilePath` text COLLATE utf8_unicode_ci NOT NULL,
  		UNIQUE KEY `ProgressID` (`ProgressID`)
		)"""
  cursor.execute(sql)
  sql = """CREATE TABLE `Student` (
  		`StudentID` int(11) NOT NULL AUTO_INCREMENT,
  		`FirstName` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  		`LastName` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  		`ClassID` int(11) NOT NULL,
  		`Email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  		`Password` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  		UNIQUE KEY `StudentID` (`StudentID`)
		)""""
  cursor.execute(sql)
  sql = """CREATE TABLE `Task` (
  		`TaskID` int(11) NOT NULL AUTO_INCREMENT,
  		`Title` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  		`Path` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  		`Tests_Results` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  		`Hints` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  		UNIQUE KEY `TaskID` (`TaskID`)
		)"""
  cursor.execute(sql)
  sql = """CREATE TABLE `Teacher` (
  		`TeacherID` int(11) NOT NULL AUTO_INCREMENT,
  		`FirstName` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  		`LastName` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  		`Email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  		`Password` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  		UNIQUE KEY `TeacherID` (`TeacherID`)
		)"""
  cursor.execute(sql)
  sql = """CREATE TABLE `TeacherClassRelationship` (
  		`TeacherClassRelID` int(11) NOT NULL AUTO_INCREMENT,
  		`ClassID` int(11) NOT NULL,
  		`TeacherID` int(11) NOT NULL,
  		UNIQUE KEY `TeacherClassRelID` (`TeacherClassRelID`)
		)"""
  cursor.execute(sql)