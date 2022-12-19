-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: cinema
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.25-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `customer_ID` int(11) NOT NULL,
  `seat_ID` int(11) NOT NULL,
  `show_ID` int(11) NOT NULL,
  `payment_ID` int(11) NOT NULL,
  KEY `fk_customer` (`customer_ID`),
  KEY `fk_show` (`show_ID`),
  KEY `fk_payment` (`payment_ID`),
  CONSTRAINT `fk_customer` FOREIGN KEY (`customer_ID`) REFERENCES `customer` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_payment` FOREIGN KEY (`payment_ID`) REFERENCES `payment` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_show` FOREIGN KEY (`show_ID`) REFERENCES `shows` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (2,10,4,3),(2,6,3,4),(2,9,4,5),(2,8,4,6),(2,10,5,7),(2,10,6,8),(3,8,3,9),(3,19,4,10),(3,9,6,11),(3,10,9,12);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'name','email','password'),(2,'Roberto','mail@mail.com','123456'),(3,'admin','admin','admin');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hall`
--

DROP TABLE IF EXISTS `hall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hall` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `theatre_ID` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  PRIMARY KEY (`ID`,`theatre_ID`),
  KEY `fk_hall` (`theatre_ID`),
  CONSTRAINT `fk_hall` FOREIGN KEY (`theatre_ID`) REFERENCES `theatre` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hall`
--

LOCK TABLES `hall` WRITE;
/*!40000 ALTER TABLE `hall` DISABLE KEYS */;
INSERT INTO `hall` VALUES (1,1,40),(2,3,40),(3,3,50),(4,4,30),(5,3,0),(6,4,20);
/*!40000 ALTER TABLE `hall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `length` time NOT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (3,'Black Panther: Wakanda Forever','00:00:02','Acción/Aventura','Español'),(4,'Black Adam','00:00:02','Acción','Español'),(5,'Top Gun: Maverick','02:11:00','Acción/Aventura','Español'),(6,'','00:00:00','',''),(7,'asd','00:00:00','asd','asd');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `amt` float NOT NULL,
  `pay_time` time NOT NULL,
  `pay_date` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,5000,'18:18:48','2022-11-24'),(2,1000,'21:37:41','2022-11-25'),(3,1000,'20:25:59','2022-11-26'),(4,800,'23:07:35','2022-11-26'),(5,1000,'23:11:50','2022-11-26'),(6,1000,'23:16:28','2022-11-26'),(7,500,'16:39:06','2022-11-27'),(8,500,'16:40:30','2022-11-27'),(9,800,'23:16:12','2022-12-10'),(10,1000,'21:58:17','2022-12-12'),(11,500,'21:58:52','2022-12-12'),(12,1000,'22:03:56','2022-12-12');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seatinline`
--

DROP TABLE IF EXISTS `seatinline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seatinline` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `seat_ID` int(11) NOT NULL,
  `show_ID` int(11) NOT NULL,
  `book_time` time NOT NULL,
  `book_date` date NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_seatShow` (`show_ID`),
  CONSTRAINT `fk_seatShow` FOREIGN KEY (`show_ID`) REFERENCES `shows` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seatinline`
--

LOCK TABLES `seatinline` WRITE;
/*!40000 ALTER TABLE `seatinline` DISABLE KEYS */;
INSERT INTO `seatinline` VALUES (10,9,3,'21:37:01','2022-12-12'),(11,20,4,'21:57:38','2022-12-12');
/*!40000 ALTER TABLE `seatinline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shows` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `movie_ID` int(11) NOT NULL,
  `hall_ID` int(11) NOT NULL,
  `theatre_ID` int(11) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `show_date` date NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_movie` (`movie_ID`),
  KEY `fk_halltheatre` (`hall_ID`,`theatre_ID`),
  CONSTRAINT `fk_halltheatre` FOREIGN KEY (`hall_ID`, `theatre_ID`) REFERENCES `hall` (`ID`, `theatre_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_movie` FOREIGN KEY (`movie_ID`) REFERENCES `movie` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES (3,3,3,3,'20:00:00','22:41:00','2022-12-30',800),(4,4,3,3,'20:30:00','22:35:00','2022-12-30',1000),(5,5,4,4,'15:00:00','17:11:00','2022-12-30',500),(6,5,4,4,'10:00:00','12:11:00','2022-12-29',500),(7,7,4,4,'00:01:23','00:01:23','2022-12-29',123),(8,3,6,4,'22:00:00','22:00:02','2022-12-30',1000),(9,5,6,4,'15:00:00','17:11:00','2022-12-31',1000);
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `theatre`
--

DROP TABLE IF EXISTS `theatre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `theatre` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `road` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theatre`
--

LOCK TABLES `theatre` WRITE;
/*!40000 ALTER TABLE `theatre` DISABLE KEYS */;
INSERT INTO `theatre` VALUES (1,'Hoyts','pincode','Salta',1),(2,'Hoyts','pincode','Salta',2),(3,'Cinemar','pincode','Salta',2),(4,'Cine Unsa','Código Postal','Salta',4400);
/*!40000 ALTER TABLE `theatre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'cinema'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13  3:38:44
