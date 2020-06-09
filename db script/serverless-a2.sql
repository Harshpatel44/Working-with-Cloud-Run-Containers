-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: serverless-a2.cdvxuztseuhu.us-east-1.rds.amazonaws.com    Database: serverless-A2
-- ------------------------------------------------------
-- Server version	5.7.22-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `userInfo`
--

DROP TABLE IF EXISTS `userInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userInfo` (
  `userName` varchar(200) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `passwd` varchar(100) DEFAULT NULL,
  `topic` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userInfo`
--

LOCK TABLES `userInfo` WRITE;
/*!40000 ALTER TABLE `userInfo` DISABLE KEYS */;
INSERT INTO `userInfo` VALUES ('harshgp44','harshgp44',';;;;','1st Option'),('testing1','testing1email','~o}~sxq;','1st Option'),('testing2','testing2email','~o}~sxq<','1st Option'),('testuser','testemail','<<<<','1st Option');
/*!40000 ALTER TABLE `userInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userState`
--

DROP TABLE IF EXISTS `userState`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userState` (
  `userName` varchar(200) NOT NULL,
  `state` varchar(10) DEFAULT NULL,
  `timeStmp` datetime DEFAULT NULL,
  PRIMARY KEY (`userName`),
  CONSTRAINT `userState_ibfk_1` FOREIGN KEY (`userName`) REFERENCES `userInfo` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userState`
--

LOCK TABLES `userState` WRITE;
/*!40000 ALTER TABLE `userState` DISABLE KEYS */;
INSERT INTO `userState` VALUES ('harshgp44','online','2020-06-08 05:31:42');
/*!40000 ALTER TABLE `userState` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09 12:56:25
