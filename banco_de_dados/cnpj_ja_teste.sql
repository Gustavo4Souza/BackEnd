-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: cnpj_ja
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `teste`
--

DROP TABLE IF EXISTS `teste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teste` (
  `Empresa` text,
  `CNPJ` text,
  `Estado` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teste`
--

LOCK TABLES `teste` WRITE;
/*!40000 ALTER TABLE `teste` DISABLE KEYS */;
INSERT INTO `teste` VALUES ('TOTVS S.A.','53113791000122','SP'),('CI&T Software S.A.','02703228000103','SP'),('Movile Internet MÃ³vel S.A.','02337024000100','SP'),('Sympla Internet S.A.','14644327000170','MG'),('Take Blip (Take.net)','04452214000152','MG'),('OLX Brasil S.A.','02748623000161','RJ'),('Globo ComunicaÃ§Ã£o e ParticipaÃ§Ãµes S.A.','27865757000102','RJ'),('EBANX S.A.','13363900000130','PR'),('Olist ServiÃ§os Digitais S.A.','20934721000102','PR'),('Resultados Digitais (RD Station)','13012372000120','SC'),('Softplan Planejamento e Sistemas','83606630000147','SC'),('Getnet Tecnologia e ServiÃ§os','04625514000144','RS'),('Zenvia Mobile ServiÃ§os Digitais','06982279000109','RS'),('In Loco Tecnologia da InformaÃ§Ã£o','11151535000179','PE'),('Tempest Security Intelligence','05265564000135','PE'),('UNICOBA IndÃºstria de Tecnologia','04321509000170','BA'),('CIMATEC â€“ Instituto SENAI de InovaÃ§Ã£o','03868202000110','BA'),('Mob Telecom','04457112000145','CE'),('Fortes Tecnologia','07455069000104','CE'),('BRISA â€“ Sociedade para o Desenvolvimento da Tecnologia da InformaÃ§Ã£o','00889104000189','DF'),('Memora Processos Inovadores','04283524000145','DF');
/*!40000 ALTER TABLE `teste` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-10 23:20:40
