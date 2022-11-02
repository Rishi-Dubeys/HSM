-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.67-community-nt


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema hms
--

CREATE DATABASE IF NOT EXISTS hms;
USE hms;


--
-- Definition of table `registration`
--


DROP TABLE IF EXISTS `registration`;
CREATE TABLE `registration` (
  `username` varchar(20) default NULL,
  `password` varchar(20) default NULL,
  `email` varchar(20) default NULL,
  `phone` varchar(20) default NULL,
  `address` varchar(20) default NULL,
  `city` varchar(20) default NULL,
  `country` varchar(20) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table `registration`

/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` (`username`,`password`,`email`,`phone`,`address`,`city`,`country`) VALUES 
 ('trttyy',']jhjh','jkjk','jkjk','kjklj','kljlkj','jlkj');
 ('komal','kim@123','kim@gmail.com','9929637418','uk-12 ,street NO -2','UK','sydney');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;


-- Definition of table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE `appointment` (
  `AppointmentID` int(10) unsigned NOT NULL auto_increment,
  `Appointmentdate` datetime default NULL,
  `Appointmenttime` varchar(45) NOT NULL,
  `DoctorID` int(11) default NULL,
  `Visit` int(11) default NULL,
  `Status` varchar(145) NOT NULL,
  PRIMARY KEY  (`AppointmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` (`AppointmentID`,`Appointmentdate`,`Appointmenttime`,`DoctorID`,`Visit`,`Status`) VALUES 
 (122,'2022-10-25 00:00:00','11pm',23,1,'Fever');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;


--
-- Definition of table `bill`
--

DROP TABLE IF EXISTS `bill`;
CREATE TABLE `bill` (
  ` Bill_number PK` int(10) unsigned NOT NULL auto_increment,
  `Patient_ID FK` varchar(45) NOT NULL,
  `Bill_Date` varchar(45) NOT NULL,
  `Bill_status` varchar(45) NOT NULL,
  PRIMARY KEY  (` Bill_number PK`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill`
--

/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;


--
-- Definition of table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
CREATE TABLE `doctor` (
  `Doctor_number` int(10) unsigned NOT NULL auto_increment,
  `Doctor_firstname` varchar(45) NOT NULL,
  `doctor_lastname` varchar(45) NOT NULL,
  `DOJ` varchar(45) NOT NULL,
  `Designation` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  PRIMARY KEY  USING BTREE (`Doctor_number`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` (`Doctor_number`,`Doctor_firstname`,`doctor_lastname`,`DOJ`,`Designation`,`mobile`,`Address`) VALUES 
 (22,'sam','jack','02/02/1999','Doctor','8529637418','32  sea beach UK'),
 (23,'Jack carter','sam','02/02/1998','Doctor','09561856345','32 Aaradhya Nagari');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;


--
-- Definition of table `lab`
--

DROP TABLE IF EXISTS `lab`;
CREATE TABLE `lab` (
  `ID` int(10) unsigned NOT NULL auto_increment,
  `PatientID` int(10) unsigned NOT NULL,
  `DoctorID` int(10) unsigned NOT NULL,
  `Test` varchar(145) NOT NULL,
  `BillAmount` double NOT NULL,
  `Billdate` datetime NOT NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lab`
--

/*!40000 ALTER TABLE `lab` DISABLE KEYS */;
INSERT INTO `lab` (`ID`,`PatientID`,`DoctorID`,`Test`,`BillAmount`,`Billdate`) VALUES 
 (1,44,23,'CBC',100,'2022-10-25 00:00:00');
/*!40000 ALTER TABLE `lab` ENABLE KEYS */;


--
-- Definition of table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient` (
  `PatientID` int(11) NOT NULL default '0',
  `AppoinmentDate` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `age` int(11) NOT NULL default '0',
  `MobileNumber` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  PRIMARY KEY  (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` (`PatientID`,`AppoinmentDate`,`FirstName`,`lastName`,`MobileNumber`,`city`,`address`,`state`) VALUES 
 (44,'25/10/2022','Jack','sam','09561856345','AUS','44 UK','UK');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;


--
-- Definition of table `patientmedicin`
--

DROP TABLE IF EXISTS `patientmedicin`;
CREATE TABLE `patientmedicin` (
  `ID` int(10) unsigned NOT NULL auto_increment,
  `DoctorID` int(10) unsigned NOT NULL,
  `PatientID` int(10) unsigned NOT NULL,
  `MedicinDetail` varchar(145) NOT NULL,
  `NextVisit` datetime NOT NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patientmedicin`
--

/*!40000 ALTER TABLE `patientmedicin` DISABLE KEYS */;
INSERT INTO `patientmedicin` (`ID`,`DoctorID`,`PatientID`,`MedicinDetail`,`NextVisit`) VALUES 
 (1,23,44,'Crosin-4days 1--1','2022-10-27 00:00:00');
/*!40000 ALTER TABLE `patientmedicin` ENABLE KEYS */;


--
-- Definition of table `payment`
--

DROP TABLE IF EXISTS `payment`;
CREATE TABLE `payment` (
  `ReceptionNo` int(10) unsigned NOT NULL auto_increment,
  `PatientID` varchar(45) NOT NULL,
  `PaymentDate` varchar(45) NOT NULL,
  `PaymentWith` varchar(45) NOT NULL,
  `Amount` decimal(10,0) NOT NULL,
  PRIMARY KEY  (`ReceptionNo`)
) ENGINE=InnoDB AUTO_INCREMENT=4579 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` (`ReceptionNo`,`PatientID`,`PaymentDate`,`PaymentWith`,`Amount`) VALUES 
 (4578,'44','25/10/2022','cash','1000');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;


--
-- Definition of table `staff`
--

DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff` (
  `staff_number` int(10) unsigned NOT NULL auto_increment,
  `staff_firstname` varchar(45) NOT NULL,
  `staff_lastname` varchar(45) NOT NULL,
  `DOJ` varchar(45) NOT NULL,
  `Designation` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  PRIMARY KEY  USING BTREE (`staff_number`)
) ENGINE=InnoDB AUTO_INCREMENT=334 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` (`staff_number`,`staff_firstname`,`staff_lastname`,`DOJ`,`Designation`,`mobile`,`Address`) VALUES 
 (22,'Jimmy','karter','03/03/1999','Doctor','8561856345','53 zoo uk'),
 (23,'Jack','sam','02/02/1999','Doctor','09561856345','32 UK');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;






/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
