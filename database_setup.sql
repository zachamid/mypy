--
-- Table structure for table `Class`
--

DROP TABLE IF EXISTS `Class`;
CREATE TABLE IF NOT EXISTS `Class` (
  `ClassID` int(11) NOT NULL AUTO_INCREMENT,
  `ClassName` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  UNIQUE KEY `ClassID` (`ClassID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;

--
-- Table structure for table `Progress`
--

DROP TABLE IF EXISTS `Progress`;
CREATE TABLE IF NOT EXISTS `Progress` (
  `ProgressID` int(11) NOT NULL AUTO_INCREMENT,
  `TaskID` int(11) NOT NULL,
  `StudentID` int(11) NOT NULL,
  `DateStarted` timestamp NULL DEFAULT NULL,
  `DateModified` timestamp NULL DEFAULT NULL,
  `DateCompleted` timestamp NULL DEFAULT NULL,
  `Output` text NOT NULL,
  `Code` text,
  `Correctness_Points` decimal(5,4) NOT NULL DEFAULT '0.0000',
  `Similarity_Points` decimal(5,4) NOT NULL DEFAULT '0.0000',
  `Attempts` int(11) NOT NULL DEFAULT '1',
  `Attempts_Points` decimal(5,4) NOT NULL DEFAULT '0.0000',
  `Time_Points` decimal(5,4) NOT NULL DEFAULT '0.0000',
  UNIQUE KEY `ProgressID` (`ProgressID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
CREATE TABLE IF NOT EXISTS `Student` (
  `StudentID` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `LastName` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ClassID` int(11) NOT NULL,
  `Email` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Password` varchar(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  UNIQUE KEY `StudentID` (`StudentID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;

--
-- Table structure for table `Task`
--

DROP TABLE IF EXISTS `Task`;
CREATE TABLE IF NOT EXISTS `Task` (
  `TaskID` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  UNIQUE KEY `TaskID` (`TaskID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;

--
-- Table structure for table `Teacher`
--

DROP TABLE IF EXISTS `Teacher`;
CREATE TABLE IF NOT EXISTS `Teacher` (
  `TeacherID` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `LastName` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Email` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Password` varchar(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Administrator` int(11) NOT NULL DEFAULT '0',
  UNIQUE KEY `TeacherID` (`TeacherID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;

--
-- Table structure for table `TeacherClassRelationship`
--

DROP TABLE IF EXISTS `TeacherClassRelationship`;
CREATE TABLE IF NOT EXISTS `TeacherClassRelationship` (
  `TeacherClassRelationshipID` int(11) NOT NULL AUTO_INCREMENT,
  `ClassID` int(11) NOT NULL,
  `TeacherID` int(11) NOT NULL,
  UNIQUE KEY `TeacherClassRelID` (`TeacherClassRelationshipID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;

--
-- Table structure for table `Tutorial`
--

DROP TABLE IF EXISTS `Tutorial`;
CREATE TABLE IF NOT EXISTS `Tutorial` (
  `TutorialID` int(11) NOT NULL AUTO_INCREMENT,
  `TutorialName` varchar(70) NOT NULL,
  `TutorialText` text NOT NULL,
  UNIQUE KEY `TutorialID` (`TutorialID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ;