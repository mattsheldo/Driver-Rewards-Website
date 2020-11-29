-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com    Database: DriverRewards
-- ------------------------------------------------------
-- Server version	8.0.17

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Dumping data for table `Admins`
--

LOCK TABLES `Admins` WRITE;
/*!40000 ALTER TABLE `Admins` DISABLE KEYS */;
INSERT INTO `Admins` VALUES ('admin'),('beatlesmagic');
/*!40000 ALTER TABLE `Admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Driver_Alerts`
--

LOCK TABLES `Driver_Alerts` WRITE;
/*!40000 ALTER TABLE `Driver_Alerts` DISABLE KEYS */;
INSERT INTO `Driver_Alerts` VALUES (15,'testuser','op','Your order has been placed'),(16,'testuser','oi','There\'s an issue with you order'),(17,'testuser','pc','Your points have been updated'),(20,'movemove','pc','Your points have been updated'),(21,'falconflyer','op','Your order has been placed');
/*!40000 ALTER TABLE `Driver_Alerts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Driver_Points`
--

LOCK TABLES `Driver_Points` WRITE;
/*!40000 ALTER TABLE `Driver_Points` DISABLE KEYS */;
INSERT INTO `Driver_Points` VALUES ('bigmoneyX',-1,0,0),('davidDrives56',-1,0,0),('dummydriver',-1,100000000,0),('dummydriver',3,100000000,1),('falconflyer',-1,0,0),('falconflyer',0,3532,1),('falconflyer',2,396772,1),('iamuser',-1,0,0),('iceroadtrucker',-1,0,0),('movemove',-1,0,0),('testuser',-1,0,0);
/*!40000 ALTER TABLE `Driver_Points` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Drivers`
--

LOCK TABLES `Drivers` WRITE;
/*!40000 ALTER TABLE `Drivers` DISABLE KEYS */;
INSERT INTO `Drivers` VALUES ('bigmoneyX',1,1,1,NULL),('davidDrives56',1,1,1,NULL),('dummydriver',1,1,1,''),('falconflyer',1,1,1,NULL),('hithere',1,1,1,NULL),('iamuser',1,1,1,NULL),('iceroadtrucker',1,1,1,NULL),('move',1,1,1,NULL),('movemove',1,1,1,NULL),('testuser',1,0,0,NULL);
/*!40000 ALTER TABLE `Drivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Employers`
--

LOCK TABLES `Employers` WRITE;
/*!40000 ALTER TABLE `Employers` DISABLE KEYS */;
INSERT INTO `Employers` VALUES (-1,'unemployed',20.00,0,'test'),(0,'Clemson',100.00,640742,'Young the Giant'),(1,'Takebook',100.00,359222,'Mario'),(2,'Microhard',100.00,925202,'Starbucks'),(3,'DummyEmployer',100.00,111111,'Van Scoy');
/*!40000 ALTER TABLE `Employers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Invoices`
--

LOCK TABLES `Invoices` WRITE;
/*!40000 ALTER TABLE `Invoices` DISABLE KEYS */;
/*!40000 ALTER TABLE `Invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Point_History`
--

LOCK TABLES `Point_History` WRITE;
/*!40000 ALTER TABLE `Point_History` DISABLE KEYS */;
INSERT INTO `Point_History` VALUES (0,'iamuser',0,'2020-11-19 22:51:57',1000,'add','testuser2',NULL),(1,'iamuser',0,'2020-11-19 22:52:01',1000,'sub','testuser2',NULL),(2,'movemove',0,'2020-11-19 22:53:14',100,'add','testuser2',NULL),(3,'falconflyer',0,'2020-11-20 09:08:20',500,'sub','newsponsor',NULL),(4,'falconflyer',0,'2020-11-20 09:43:54',7000,'sub','newsponsor',NULL),(5,'falconflyer',2,'2020-11-20 09:45:06',3228,'sub',NULL,'beatlesmagic'),(6,'falconflyer',0,'2020-11-22 12:57:12',17468,'sub',NULL,'beatlesmagic');
/*!40000 ALTER TABLE `Point_History` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Purchase_History`
--

LOCK TABLES `Purchase_History` WRITE;
/*!40000 ALTER TABLE `Purchase_History` DISABLE KEYS */;
INSERT INTO `Purchase_History` VALUES (0,'falconflyer',1,'2020-11-09 22:11:24',250,'Custom Instagram Snapchat Twitter Youtube TikTok Facebook Vinyl Decal Sticker',NULL,NULL,283785259866),(2,'falconflyer',1,'2020-11-13 10:24:51',24500,'NEW Facebook - Portal TV Smart Video Calling w/ Alexa - Black ???? FAST SHIPPING',NULL,NULL,153949751927),(3,'falconflyer',0,'2020-11-17 16:01:23',3500,'Pikachu libre Pokemon go mega rare','newsponsor',NULL,383806820737),(4,'falconflyer',2,'2020-11-20 09:45:06',3228,'Starbucks - Reusable Hot Cups - 6 Pack - 2020 Holiday Color Changing Candy Cane',NULL,'beatlesmagic',293748818458),(5,'falconflyer',0,'2020-11-22 12:57:12',2318,'Clemson Tigers Women\'s Leggings Small to 2X-Large Cage',NULL,'beatlesmagic',402526490340),(6,'falconflyer',0,'2020-11-22 12:57:12',15150,'Xbox One 1TB Black Console',NULL,'beatlesmagic',353284278977);
/*!40000 ALTER TABLE `Purchase_History` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Shopping_Cart_Items`
--

LOCK TABLES `Shopping_Cart_Items` WRITE;
/*!40000 ALTER TABLE `Shopping_Cart_Items` DISABLE KEYS */;
INSERT INTO `Shopping_Cart_Items` VALUES (0,'iamuser',0,1695,NULL,NULL,151239684662,'Pokemon Card Lot 100 OFFICIAL TCG Cards Ultra Rare Included - GX EX MEGA + HOLOS');
/*!40000 ALTER TABLE `Shopping_Cart_Items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Sponsors`
--

LOCK TABLES `Sponsors` WRITE;
/*!40000 ALTER TABLE `Sponsors` DISABLE KEYS */;
INSERT INTO `Sponsors` VALUES ('dummysponsor',3,'admin'),('klathy',2,NULL),('newsponsor',0,NULL),('sponsor',-1,NULL),('sponsoruser',1,NULL),('testuser2',0,NULL);
/*!40000 ALTER TABLE `Sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add profile',7,'add_profile'),(26,'Can change profile',7,'change_profile'),(27,'Can delete profile',7,'delete_profile'),(28,'Can view profile',7,'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$eIvaau7benDw$swfEheb+OrRY6Caya2wIJOh+bL6yXTOycxJODpjMLME=','2020-11-27 21:01:34.889604',1,'admin','adihopethisworks','name','admin@gmail.com',1,1,'2020-09-27 19:50:40.086119','1234567890','123 Me St','yeahok'),(2,'pbkdf2_sha256$216000$RMYKmhBlwbwb$vfAU6dWpPupmj/4J2oGDgFv0rZC3eTQiZOFiTdP8fCo=','2020-11-22 16:27:03.057302',0,'iamuser','iam','name','test@gmail.com',0,1,'2020-09-27 19:58:22.001795','1112223333','456 You St','gack'),(45,'pbkdf2_sha256$216000$xoiMCusQ7rB1$lqoq0e1pXrm/8fj9b9lpMhuwDt5Tjf3BER0QmuMOxtU=','2020-11-13 19:31:22.873325',0,'testuser','tes','test','test@gmail.com',0,1,'2020-10-02 14:00:28.042183','te','te','test'),(46,'pbkdf2_sha256$216000$dYBA0aMq9mkU$mOI+UEk/nRHRSGYc/x1a7hMj8esTeE8Tl3dksspf2aU=','2020-11-27 21:01:13.931396',0,'testuser2','test','test','test@gmail.com',0,1,'2020-10-02 14:01:27.770509','3213214321','test','test'),(48,'pbkdf2_sha256$216000$GeldbXmRYTOP$uY3IxdxOQXBW+30tJD1yJjagNOt9vWN4GbZ39QVPOR8=','2020-10-11 16:15:01.890800',0,'iceroadtrucker','Ray','Flowers','iceroadtrucker@gmail.com',0,1,'2020-10-11 16:14:56.939558','1800123123','Lot 6 Sunnyvale Trailer Park, Nova Scotia','Ray'),(49,'pbkdf2_sha256$216000$N2GnY4gxN5bi$jb6I69EKriobgRgP2J7iJgiP5Cm7gnU/sdzg/aJEozA=','2020-11-10 15:17:20.047057',0,'imnewhere','Bob','Jones','new@gmail.com',0,1,'2020-10-12 20:59:40.347617','8036541234','123 I Live Here','Bobby'),(50,'pbkdf2_sha256$216000$7W0a8wI1Czmw$5bEhNtnrz0mL/SO9wjENruY52PHEk0TVJ3t5Swxof9Q=',NULL,0,'iamnew','bill','jones','new@gmail.com',0,1,'2020-10-12 21:02:36.607052','654803654','123 Me Street','billy'),(53,'pbkdf2_sha256$216000$bixqekDncFpw$SzX9I2lhClR3AmIX1wVReay7KAhRscd9E8OLpoMb8Wo=','2020-11-09 22:36:37.150899',0,'hithere','try','test','test@gmail.com',0,1,'2020-10-12 21:28:17.338341','3213214321','162 Stephenson Ln','test'),(54,'pbkdf2_sha256$216000$Llryco0L7Yj3$bNgNDhAA6Tr5Pf3XoBSNISdMKKYO/csbfMkUpeHgSaQ=','2020-10-15 16:49:26.059498',0,'move','o','m','move@clemson.edu',0,1,'2020-10-15 16:49:18.839735','m','m','m'),(55,'pbkdf2_sha256$216000$UQWfjrNy2Gh4$WItJYnmWIswnsoZh7uF9jSga++bJjeN8Dluq6Iig/Vw=','2020-11-20 03:54:16.303469',0,'movemove','movenow','jklj','hi@gmail.com',0,1,'2020-10-15 16:56:01.993059','jkl','jkl','jklj'),(56,'pbkdf2_sha256$216000$bYxsRuH4AmuQ$+ra5wWpo+6G7fTZrCLUAwcXG5UyUVPOX7+3uDhyLtN4=',NULL,0,'sponsor','tjeks','tjdks','test@gmail.com',0,1,'2020-10-16 22:27:47.213013','djsk','djsk','jddks'),(57,'pbkdf2_sha256$216000$8GupLZlvn8FQ$FI8RKWLPGWMCEQ71xOfy4svl2UaJh18Hai/0Ox7/HLY=','2020-11-13 15:32:10.245405',0,'sponsoruser','Jack','Sparrow1','sp@gmail.com',0,1,'2020-10-19 01:06:57.643963','8037771234','134 Caribbean Way','Captain'),(58,'pbkdf2_sha256$216000$CtxVUlEHMK2q$OdTSTHUSG1E84UEkIdoySNubqrpyLDPebsmANRr0IVA=','2020-11-20 14:50:03.980296',0,'falconflyer','Han','Solo','hsolo@yahoo.com',0,1,'2020-10-19 19:53:42.412531','8030000001','Do Not Find Me St','Han'),(59,'pbkdf2_sha256$216000$IV7M500wo5dp$CRHhNluY5tYmZbBkAGIh7+furJc2qOT8TYCd2utzbDg=','2020-11-28 15:33:51.869858',0,'newsponsor','new','sponsor','new@gmail.com',0,1,'2020-10-23 14:26:10.547654','8031234123','street','new'),(60,'pbkdf2_sha256$216000$WAQwR6mtgVW1$17ozwGJDBMnv63tbxtcQcpAv+YAFclfFYN0C2jwv5DE=',NULL,0,'davidDrives57','David','Jones','david@gmail.com',0,1,'2020-10-24 14:51:13.109571','(864)-999-','123 Street St','Dave'),(61,'pbkdf2_sha256$216000$9bK0pcRaYgJq$R/2ZX/0pHyCNXPaeilziIN926lnDONFccwu8V8BuBM4=',NULL,0,'davidDrives56','David','Jones','david@gmail.com',0,1,'2020-10-24 14:54:14.247627','(864)-999-','123 Street St','Dave'),(63,'pbkdf2_sha256$216000$uHCBq5qHkxco$z+aKDC/6bwH4yCH340xaeYXU3gdBjmpEH3QRM2Tsljk=','2020-11-16 15:26:28.675053',0,'klathy','Kathy','Lathy','kathy.lathy@yahoo.com',0,1,'2020-10-27 01:05:37.481344','8038781100','101 Kathy St','K'),(64,'pbkdf2_sha256$216000$noF3CbIDC52M$MZjS8Zbf3UWWin1i7dCfIcp7wQhNcm2RgHGgPcSghjs=','2020-11-29 19:55:25.412460',0,'beatlesmagic','Paul','Lennon','new@gmail.com',0,1,'2020-10-30 14:45:44.006771','8645550000','Penny Lane','P'),(65,'pbkdf2_sha256$216000$XfITDsimWEPs$ynhlOMLw6zi1Ri3m9PQC6DnVj1SEdWt1q28c2vIDYlw=','2020-10-31 14:36:13.181905',0,'bigmoneyX','youngslock','g','shmoney@getit.com',0,1,'2020-10-31 14:36:01.863542','8033214321','Mean St','lizard'),(66,'pbkdf2_sha256$216000$njug6DDV7Xog$DWkAER4c/0U7hEtgpDUbk4G5h1J4QKeEXVEmDAg6Y+0=','2020-11-27 21:01:37.849389',0,'dummydriver','Dummy','Driver','fake@gmail.com',0,1,'2020-11-16 14:43:41.458958','(999)999-9','123 I Live Here','Driver'),(67,'pbkdf2_sha256$216000$myUfctuG3JyZ$znTZ7ktzaa4IBxwKlOIwokFzP2I1cbFaQWnlPbSUkOo=','2020-11-27 21:01:39.318506',0,'dummysponsor','Dummy','Sponsor','fake@gmail.com',0,1,'2020-11-16 14:44:34.614557','(555)555-5','123 Me Street','Spons');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-09-28 19:13:10.398464','3','blabla',3,'',4,1),(2,'2020-10-01 15:21:18.634100','8','alsouser4',3,'',4,1),(3,'2020-10-01 15:21:25.944323','7','alsouser3',3,'',4,1),(4,'2020-10-01 15:21:32.287051','6','alsouser2',3,'',4,1),(5,'2020-10-01 15:21:38.364355','5','alsouser',3,'',4,1),(6,'2020-10-01 15:36:41.241285','10','alsouser2',3,'',4,1),(7,'2020-10-01 15:36:48.738960','9','alsouser',3,'',4,1),(8,'2020-10-01 15:41:57.677404','13','alsouser3',3,'',4,1),(9,'2020-10-01 15:42:04.646739','12','alsouser2',3,'',4,1),(10,'2020-10-01 15:42:13.729698','11','alsouser',3,'',4,1),(11,'2020-10-01 16:01:56.408512','15','test2',3,'',4,1),(12,'2020-10-01 16:02:03.050686','14','test',3,'',4,1),(13,'2020-10-01 16:13:25.677739','16','test3',3,'',4,1),(16,'2020-10-01 17:37:38.964098','20','neverseen',3,'',4,1),(17,'2020-10-01 17:37:50.791080','19','tester',3,'',4,1),(18,'2020-10-01 17:38:04.057654','17','alsouser',3,'',4,1),(20,'2020-10-01 17:46:04.434836','21','newtest',3,'',4,1),(21,'2020-10-01 17:46:11.264077','22','fill',3,'',4,1),(22,'2020-10-01 19:36:54.307081','23','plzwork',3,'',4,1),(23,'2020-10-01 19:37:03.790540','25','test2',3,'',4,1),(25,'2020-10-01 19:37:30.993054','24','tryagain',3,'',4,1),(26,'2020-10-01 23:58:53.334124','31','tjksfkdslj',3,'',4,1),(27,'2020-10-01 23:59:01.536339','29','goagain',3,'',4,1),(28,'2020-10-01 23:59:09.406671','27','newtest',3,'',4,1),(29,'2020-10-01 23:59:16.963440','28','test',3,'',4,1),(30,'2020-10-01 23:59:24.393003','30','trythree',3,'',4,1),(31,'2020-10-01 23:59:31.297018','32','testuser',3,'',4,1),(32,'2020-10-02 00:08:52.950869','33','testuser',3,'',4,1),(33,'2020-10-02 00:10:57.439399','34','testuser',3,'',4,1),(34,'2020-10-02 00:13:14.732269','35','testuser',3,'',4,1),(35,'2020-10-02 00:18:06.608083','36','testuser',3,'',4,1),(36,'2020-10-02 00:22:15.127714','37','testuser',3,'',4,1),(37,'2020-10-02 00:27:28.455285','38','testuser',3,'',4,1),(38,'2020-10-02 00:29:33.572548','39','testuser',3,'',4,1),(39,'2020-10-02 00:34:00.580264','40','testuser',3,'',4,1),(40,'2020-10-02 00:37:23.078856','41','testuser',3,'',4,1),(44,'2020-10-02 14:03:54.981628','47','admin2',1,'[{\"added\": {}}]',4,1),(45,'2020-10-12 21:22:54.902248','51','tryagain',3,'',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'main','profile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-09-24 16:06:46.518440'),(2,'auth','0001_initial','2020-09-24 16:06:46.755193'),(3,'admin','0001_initial','2020-09-24 16:06:47.308993'),(4,'admin','0002_logentry_remove_auto_add','2020-09-24 16:06:47.448414'),(5,'admin','0003_logentry_add_action_flag_choices','2020-09-24 16:06:47.463170'),(6,'contenttypes','0002_remove_content_type_name','2020-09-24 16:06:47.583968'),(7,'auth','0002_alter_permission_name_max_length','2020-09-24 16:06:47.664588'),(8,'auth','0003_alter_user_email_max_length','2020-09-24 16:06:47.698339'),(9,'auth','0004_alter_user_username_opts','2020-09-24 16:06:47.714451'),(10,'auth','0005_alter_user_last_login_null','2020-09-24 16:06:47.772514'),(11,'auth','0006_require_contenttypes_0002','2020-09-24 16:06:47.781343'),(12,'auth','0007_alter_validators_add_error_messages','2020-09-24 16:06:47.796023'),(13,'auth','0008_alter_user_username_max_length','2020-09-24 16:06:47.873052'),(14,'auth','0009_alter_user_last_name_max_length','2020-09-24 16:06:47.948980'),(15,'auth','0010_alter_group_name_max_length','2020-09-24 16:06:47.980045'),(16,'auth','0011_update_proxy_permissions','2020-09-24 16:06:48.000160'),(17,'auth','0012_alter_user_first_name_max_length','2020-09-24 16:06:48.085763'),(18,'sessions','0001_initial','2020-09-24 16:06:48.125173'),(19,'main','0001_initial','2020-09-29 17:05:59.671583'),(20,'main','0002_delete_profile','2020-10-01 20:35:47.113071');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('08bemc4uwxdr0j6ccj70dnv10o7qrzn6','.eJxVjDsOwjAQBe_iGlnxOv5R0nMGa71r4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZjEacfseE9MhtJ3zHdpslzW1dpiR3RR60y-vM-Xk53L-Dir1-a4QUDKMj0kYDs7JDcUoZQuWCKaxzKMEGnYqirBODt4P3MIIvVkEB8f4AEws34Q:1kPwQp:jLJqBRoPEIrOEofCogMuFK2uswMUZ7uLZH0wlgPUV-E','2020-10-20 23:31:43.769161'),('9pxpiws1jwbw80qgu6s9cykcxznr0hvx','e30:1kNJW6:WS-Pc4Fvzs7Ge8LDellOYTbf5NzehDNLcKhssSsPeSw','2020-10-13 17:34:18.860858'),('djxp73bf21dt9xs87puvmr9n4mbdah15','e30:1kf3ep:-2MXV_NUmYht1vvUpL2egdD22nluQTvFgnV-4Ov6Q_s','2020-12-01 16:16:39.016900'),('eoh41y77kk4eaaepp7v7hksgxrbguu0r','e30:1kNJff:mmHvQ47ns1LjEHr6fDTepajOIe0_EX1nc4OLR55bl3E','2020-10-13 17:44:11.561861'),('g9ldc9eycone41c69grn4tjes9ovsvbo','.eJxVjMsOwiAQRf-FtSEUHB4u3fcbyDAwUjU0Ke3K-O_apAvd3nPOfYmI21rj1ssSpywuwjpx-h0T0qO0neQ7ttssaW7rMiW5K_KgXY5zLs_r4f4dVOz1WyMYjZ5ZmRKAFHFOQAEcsfcKIA3OZp0CcMA08LkYRVpro4JjtJ6yeH8AH8M4dA:1kg8Fz:2Fh1DoivGwuXqjZ9hp6dGwzXYl5WZalnqEGzOUchj38','2020-12-04 15:23:27.787052'),('is741sftrvbvaki74xh89d4ivbktmrjl','.eJxVjEEOwiAQRe_C2hBgQIpL9z0DGYapVA0kpV0Z765NutDtf-_9l4i4rSVunZc4Z3ERWpx-t4T04LqDfMd6a5JaXZc5yV2RB-1ybJmf18P9OyjYy7cmY3ywgBa8R2DFwzAxJdIaIMB0doxAPgUgqyFzQGsCKeWyMsGRt-L9AdfpN28:1kf3Ej:a2NHvPrZYqQPJUgDN-VGnJRypf5a4uiMGPrAbYOSrQw','2020-12-01 15:49:41.537667'),('j6tcbgkdshuvyw07t26otfqs4yuef4yi','.eJxVjEEOwiAQRe_C2hBgQIpL9z0DGYapVA0kpV0Z765NutDtf-_9l4i4rSVunZc4Z3ERWpx-t4T04LqDfMd6a5JaXZc5yV2RB-1ybJmf18P9OyjYy7cmY3ywgBa8R2DFwzAxJdIaIMB0doxAPgUgqyFzQGsCKeWyMsGRt-L9AdfpN28:1kfzsw:_irfAwr1WkxJbiFOLULgB_xUYFUMEQ5t5gK2vCQmWto','2020-12-04 06:27:06.391251'),('kgpdhcqbgjw4yu1pqdmezhnupov1yxxc','e30:1kf3Pd:iFudwj9uPmqwIQyexhPiLcPYRevfQOp_YK99QwfoOuA','2020-12-01 16:00:57.376122'),('l1a2bolu7u80xn4cmm1rloic3b9xfdgw','e30:1kemJO:k5si0bQ6zbLC2-XlqYC5MfXl5EwwtAdiWzKtI7kGR5A','2020-11-30 21:45:22.274807'),('mvqqeufiqiupjnefzo3sdtlwo9fwz78x','e30:1kemH1:qNGqMcnRtdA3w_z4u0S3UD0AXL0r6aWYOS0f3YvxkkQ','2020-11-30 21:42:55.131351'),('nssawv64ju0r1zozi4h1mbp29bgiyigq','e30:1kf3RW:kYBpNjgRoYQjVoyhEl5h_6axBTzfotAPQ3w0cPRahJg','2020-12-01 16:02:54.198998'),('p66coulu8klkecmo4mt1nb1wf3oxks1d','e30:1kNJp0:lzBUHZN4-A0nxHyBKn7qkc1qUfTWpMeaxWb9Le3NohQ','2020-10-13 17:53:50.851453'),('py2z7mfkonb9chebbko3c5zibj7b3eul','.eJxVjDsOwjAQBe_iGlnxsv5R0ucM1tpe4wBypDipEHeHSCmgfTPzXiLQttawdV7ClMVFoBGn3zFSenDbSb5Tu80yzW1dpih3RR60y3HO_Lwe7t9BpV6_tbURButdcR6zL2yUYleGFDMVoxyXZAtHhoRaJQQEddbGAhITeNAo3h8Xdjgb:1kTR5R:jmsF6Qji2GwJkxbQ3Re-HynvcbO__onrugj6GSzxaZs','2020-10-30 14:52:05.035828'),('t321t407mlrgx5g9169amej5sc4ipx5e','e30:1kNJg0:4-mELJyotf09FFsj3CjKCJYJk4IAupPD5EgvfHne4Pg','2020-10-13 17:44:32.183693'),('udjiheoq9shzyqb9ts41nt2dhu924ybk','.eJxVjEEOwiAQRe_C2hBgQIpL9z0DGYapVA0kpV0Z765NutDtf-_9l4i4rSVunZc4Z3ERWpx-t4T04LqDfMd6a5JaXZc5yV2RB-1ybJmf18P9OyjYy7cmY3ywgBa8R2DFwzAxJdIaIMB0doxAPgUgqyFzQGsCKeWyMsGRt-L9AdfpN28:1kf0uJ:c2rQw5aSbpeIynmNXSEfnY0jKe38iNkdmOwt36NoxK0','2020-12-01 13:20:27.791380'),('x10m48j67kmmf9dzk7k5ld0m4z3qy05j','e30:1kNJWa:bLcqOz2VunphIvYTC7-k52sTKlDfcFkpOprmTceL8SY','2020-10-13 17:34:48.412608'),('yedhrfspl8dyhzxvgjq98rfyj07ak1yx','.eJxVjDkOwjAUBe_iGlm245WSnjNY_otxACVSnFSIu0OkFNC-mXkvkcu2trx1XvJI4ixsFKffEQo-eNoJ3ct0myXO07qMIHdFHrTL60z8vBzu30ErvX1rhRG0p8SAyrI1RkXDjrVzfghJ1xjRE7CvgzOegq2UQMFQwWkMmIJ4fwAGZDgc:1kRdzx:KdCzcH1fiWKOELd6YYbUIBXTp3vIb69noeiZznXwaKQ','2020-10-25 16:15:01.898061'),('yja5pd2co3iygs0pmztr1bvl0mah6xzy','e30:1kemFI:2srzshq5npevo90VTIcPE1pK8z-hAugHGESUfugSIXw','2020-11-30 21:41:08.288010'),('zwb32mflmqz40cr3wmv114orgwhcjn1o','.eJxVjDsOwjAQBe_iGlnxOv5R0nMGa71r4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZjEacfseE9MhtJ3zHdpslzW1dpiR3RR60y-vM-Xk53L-Dir1-a4QUDKMj0kYDs7JDcUoZQuWCKaxzKMEGnYqirBODt4P3MIIvVkEB8f4AEws34Q:1kPwQY:w4QNTCOMk871TRbMgmWAp1VUic8gm2WUwwpq9MYmL6Q','2020-10-20 23:31:26.333994');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-29 15:26:44
