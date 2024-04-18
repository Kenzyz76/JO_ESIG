--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Olympiques;

CREATE DATABASE Olympiques CHARACTER SET 'utf8';

USE Olympiques;

--
-- Création des tables :
--

CREATE TABLE Pays (
	pays_id INT UNSIGNED NOT NULL,
	pays_nom VARCHAR(30) NOT NULL,
	pays_continent VARCHAR(30) NOT NULL,
	PRIMARY KEY (pays_id)
)
ENGINE=INNODB;

CREATE TABLE Disciplines (
	dis_id INT UNSIGNED NOT NULL,
	dis_nom VARCHAR(30) NOT NULL,
	dis_stade VARCHAR(30),
	PRIMARY KEY (dis_id)
)
ENGINE=INNODB;

CREATE TABLE Athletes (
	ath_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	ath_nom VARCHAR(30) NOT NULL,
    ath_prenom VARCHAR(30) NOT NULL, 
	ath_naissance DATE,
	ath_pays INT UNSIGNED NOT NULL,
	ath_discipline INT UNSIGNED NOT NULL,
	ath_recompense INT UNSIGNED,
    FOREIGN KEY (ath_pays) REFERENCES Pays(pays_id),
	FOREIGN KEY (ath_discipline) REFERENCES Disciplines(dis_id)
)
ENGINE=INNODB;

CREATE TABLE Recompenses (
	rec_athlete INT UNSIGNED,
	rec_discipline INT UNSIGNED,
	FOREIGN KEY (rec_athlete) REFERENCES Athletes(ath_id),
	FOREIGN KEY (rec_discipline) REFERENCES Disciplines(dis_id)
)
ENGINE=INNODB;

CREATE TABLE Visiteurs (
	vis_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	vis_nom VARCHAR(30) NOT NULL,
	vis_prenom VARCHAR(30) NOT NULL,
	vis_numero INT UNSIGNED
)
ENGINE=INNODB; 
--
-- Insertion de valeurs dans les tables :
--
INSERT INTO Pays
VALUES	(1, 'FRANCE', 'EUROPE'),
	(2, 'ALGÉRIE', 'AFRIQUE'),
	(3, 'JAMAÏQUE', 'AMÉRIQUE'),
	(4, 'JAPON', 'ASIE'),
	(5, 'CHINE', 'ASIE');
INSERT INTO Disciplines
VALUES	(1, 'JUDO', 'Arena_Champ-de-Mars'),
	(2, 'NATATION', 'Paris_La_Défense_Arena'),
	(3, 'TENNIS_DE_TABLE', 'Arena_Paris_Sud_4'),
	(4, 'ATHLETISME', 'Stade_de_France'),
	(5, 'GYMNASTIQUE_ARTISTIQUE', 'Arena_Bercy');
INSERT INTO Athletes	
VALUES	(1, 'RINER','Teddy','1989-04-07', 1, 1, NULL),
	(2, 'MARCHAND','Léon','2002-05-17',1, 2, NULL),
	(3, 'LEBRUN','Félix', '2006-09-12',1, 3, NULL),
	(4, 'DRISS','Messaoud', '2001-09-13',2, 1, NULL),
	(5, 'SEDJATI', 'Djamel','1999-05-03',2, 4, NULL),
	(6, 'MOULA', 'Slimane','1999-02-25', 2, 4, NULL),
	(7, 'FRASER-PRYCE', 'Shelly-Ann','1986-12-27',3, 4, NULL),
	(8, 'THOMPSON-HERAH', 'Elaine', '1992-06-28', 3, 4, NULL),
	(9, 'BOLT', 'Usain', '1986-08-21', 3, 4, NULL),
	(10, 'ABE', 'Uta', '2000-07-14', 4, 1, NULL),
	(11, 'ITO', 'Mima', '2000-10-21', 4, 3, NULL),
	(12, 'ABE', 'Hifumi', '1997-08-09', 4, 1, NULL),
	(13, 'ZHENDONG', 'Fan', '1997-01-22', 5, 3, NULL),
	(14, 'YUFEI', 'Zhang', '1998-04-19', 5, 2, NULL),
	(15, 'RUOTENG', 'Xiao', '1996-01-30', 5, 5, NULL);
INSERT INTO Visiteurs	
VALUES	(1, 'THIERRY','Nicolas',NULL),
	(2, 'MICHEL','Baptiste',NULL),
	(3, 'NARCISSE','Jolann',NULL),
	(4, 'DARDINIER','Foucauld',NULL),
	(5, 'CARPENTIER','Gaulthier',NULL),
	(6, 'ALLAM','Kenzi',NULL),
	(7, 'DEBERGNE','Dylan',NULL);
	
-- 
-- Requêtes :
--

 
SELECT *
FROM Visiteurs





