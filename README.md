# JO_ESIG
Titre du sujet : Jeux Olympiques 

Objectifs : 
	Dans ce projet nous avons pour but de créer une interface graphique partagée entre visiteurs et athlètes. Pour cela nous créerons une base de données propre à ce sujet afin de l’utiliser avec un programme Python.
	En résumé, si l’on s’identifie comme un visiteur celui-ci pourra consulter son billet des JO ou s’il n’en a pas, on lui proposera de s’en procurer un. Celui-ci pourra également consulter une map des JO et consulter les informations des athlètes en renseignant soit un nom d’athlète, soit une discipline, soit un pays.
	Concernant les athlètes, une fois identifier celui-ci pourra consulter ses récompenses, sa discipline, son pays. Et s’il le veut celui d’un autre pays en précisant ce dernier.

Fonctionnalités détaillées : Les fonctions que nous allons programmer vont se coller à nos objectifs cités ci-dessus mais surtout se poser sur des Classes créée à partir de notre base de données. Exemple avec la table V1 de notre base de données :

 


<img width="454" alt="image" src="https://github.com/Kenzyz76/JO_ESIG/assets/92575631/42c5142b-3f3b-4e6f-9bdf-443ab2b8aae5">





IHM :
 


<img width="223" alt="image" src="https://github.com/Kenzyz76/JO_ESIG/assets/92575631/d11f8839-1642-4d23-ae72-10247d8e7ff7">

<img width="226" alt="image" src="https://github.com/Kenzyz76/JO_ESIG/assets/92575631/085d9315-0eb2-4cc4-8104-229f212e60e5">


<img width="210" alt="image" src="https://github.com/Kenzyz76/JO_ESIG/assets/92575631/12dd18ff-3bc5-4a7b-8300-88e3ba8cc611">

<img width="197" alt="image" src="https://github.com/Kenzyz76/JO_ESIG/assets/92575631/9653abeb-419f-47dc-9309-0469e777f29a">






Fichiers pythons que l’on va utiliser :

class.py :
Répertorie les différentes classes (athlètes, pays, disciplines, visiteurs, récompenses) avec les différentes méthodes de chaque classe.

main.py :
Ce programme permettra de réutiliser ces différentes classes grâce à l’appel de modules et donc de les utiliser pour nos différentes fonctionnalités choisies. Dans ce programme on ajoutera également la programmation de l’interface graphique ou peut-être dans un autre fichier python.

athlètes.py
Ce fichier permettra d’appeler les différentes fonctions qu’on utilisera dans le menu « Athlète » tel que l’affichage du nom, prénom, pays, etc., de l’athlète en question

visiteur.py
Ce fichier nous permettra d’appeler les différentes fonctions qu’on utilisera dans le menu « Visiteurs » tel que l’affichage du nom, prénom et le numéro de billet de la personne qui se connecte.
Dates :	Objectifs :
26 MARS 2024 – 3H	- terminer la base de données (Kenzi)
- création des différentes classes (Dylan)
28 MARS 2024 – 2H	- terminer les classes (Dylan)
- commencer le programme avec les fonctions principales (Kenzi)
08 AVRIL 2024 – 3H	- continuer le programme avec l’utilisation de ces fonctions (Dylan)
- création d’une première interface graphique BETA pour visualiser les résultats des fonctions (Kenzi)
18 AVRIL 2024 – 2H	- Epurer notre interface graphique (Kenzi)
- continuer le programme (Dylan)
23 MAI 2024 – 3H	- création de l’interface graphique finale (Kenzi)
- finalisation du programme (Dylan)
27 MAI 2024 – 2H	- finitions des détails graphiques, du programme en ajoutant un maximum de commentaires (Kenzi)
- création du contre-rendu indicatif du travail effectué (Dylan)
Planning prévisionnel :
![image](https://github.com/Kenzyz76/JO_ESIG/assets/92575631/90c3678e-eaed-4278-b434-9bd2e943f42d)
