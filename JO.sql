--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Olympiques;# onvérifie d'abord si une base de données nommée "Olympiques" existe déjà. Si c'est le cas, on l'a supprime.

CREATE DATABASE Olympiques CHARACTER SET 'utf8'; #on créer la BDD dans le langage UTF-8, le langage le plus universel pour MySQL

USE Olympiques;#on se place dans cette BDD pour effectuer les prochaines lignes de codes

--
-- Création des tables :
--

CREATE TABLE Pays (
	pays_id INT UNSIGNED NOT NULL,
	pays_nom VARCHAR(30) NOT NULL,
	PRIMARY KEY (pays_id)
)
ENGINE=INNODB;#on utilise le moteur de stockage INNODB pour enregistrer notre table dans la base de donnée

CREATE TABLE Disciplines (
	dis_id INT UNSIGNED NOT NULL,
	dis_nom VARCHAR(30) NOT NULL,
	dis_stade VARCHAR(30),
	PRIMARY KEY (dis_id)
)
ENGINE=INNODB;#on utilise le moteur de stockage INNODB pour enregistrer notre table dans la base de donnée

CREATE TABLE Athletes (
	ath_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, #auto-increment pour que MySQL génére automatique les id de 1 à ...,primary key on spécifie que c'est la clé primaire de la table
	ath_nom VARCHAR(30) NOT NULL,
    ath_prenom VARCHAR(30) NOT NULL, 
	ath_naissance DATE,
	ath_pays INT UNSIGNED NOT NULL,
	ath_discipline INT UNSIGNED NOT NULL,
	ath_recompense VARCHAR(30),
    FOREIGN KEY (ath_pays) REFERENCES Pays(pays_id), #pour s'assurer à bien faire le lien entre la clé étrangère ath_pays et la clé primaire pays_id
	FOREIGN KEY (ath_discipline) REFERENCES Disciplines(dis_id) #pour s'assurer à bien faire le lien entre la clé étrangère ath_discipline et la clé primaire dis_id
)
ENGINE=INNODB;#on utilise le moteur de stockage INNODB pour enregistrer notre table dans la base de donnée

CREATE TABLE Visiteurs (
	vis_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,#auto-increment pour que MySQL génére automatique les id de 1 à ...,primary key on spécifie que c'est la clé primaire de la table
	vis_nom VARCHAR(30) NOT NULL,
	vis_prenom VARCHAR(30) NOT NULL,
	vis_numero VARCHAR(30) NOT NULL
)
ENGINE=INNODB; #on utilise le moteur de stockage INNODB pour enregistrer notre table dans la base de donnée

--
-- Insertion de valeurs dans les tables :
--
INSERT INTO Pays
VALUES	(1, 'FRANCE'),
	(2, 'ALGÉRIE'),
	(3, 'JAMAÏQUE'),
	(4, 'JAPON'),
	(5, 'CHINE');
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
VALUES	(1, 'THIERRY','Nicolas','A698736489'),
	(2, 'MICHEL','Baptiste','B235746248'),
	(3, 'NARCISSE','Jolann','C672349820'),
	(4, 'DARDINIER','Foucauld','D574136209'),
	(5, 'CARPENTIER','Gaulthier','E412670987'),
	(6, 'ALLAM','Kenzi','F159036715'),
	(7, 'DEBERGNE','Dylan','G753429861');	

-- 
-- Requêtes :
--
 
SELECT *
FROM Visiteurs





