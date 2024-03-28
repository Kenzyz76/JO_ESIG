from athlete import Athlete #on appel les différentes classes dans les différents modules
from visiteur import Visiteur
from pays import Pays
from mysql.connector import connect
dic_ath={}
dic_vis={}
class Administrateur:
    def connection(self): #on créer une fonction qui permet de se connecter à Uwamp et ainsi avoir accès à notre base de donnée
        a=connect(host="localhost",user="root",
                    password="root",database="Olympiques")
        return(a)

    def lire_athlete(self):
        b=self.connection() 
        cursor=b.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT ath_nom, ath_prenom, ath_naissance, Pays.pays_nom, ath_discipline, ath_recompense FROM Athletes INNER JOIN Pays ON Athletes.ath_pays=Pays.pays_id") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for iathlete in resultat: #on parcours le tuple1 
            nom, prenom, naissance, pays, discipline, recompense= iathlete #on assigne à chaque valeur du tuple une variable sous forme de nom
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense) #on créer (instancie) un athlète
            dic_ath[nom+" "+prenom]=athlete0 #on ajoute l'athlete à notre dico d'athlete
        for cle in dic_ath:#on parcours notre liste pour l'afficher
            print(dic_ath[cle].afficher())

    def lire_visiteur(self):
        b=self.connection() 
        cursor=b.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT vis_nom, vis_prenom, vis_numero FROM Visiteurs") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for ivisiteurs in resultat: #on parcours le tuple1 
            nom, prenom, numero= ivisiteurs #on assigne à chaque valeur du tuple une variable sous forme de nom
            visiteur0=Visiteur(nom,prenom,numero) #on créer (instancie) un visiteur
            dic_vis[nom+" "+prenom]=visiteur0#on ajoute l'athlete à notre dico de visiteur
        for cle in dic_vis:#on parcours notre liste pour l'afficher
            print(dic_vis[cle].afficher())

    def lire_athlete_search(self):
        b=self.connection() 
        cursor=b.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT ath_nom, ath_prenom, ath_naissance, Pays.pays_nom, ath_discipline, ath_recompense FROM Athletes INNER JOIN Pays ON Athletes.ath_pays=Pays.pays_id") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for iathlete in resultat: #on parcours le tuple1 
            nom, prenom, naissance, pays, discipline, recompense= iathlete #on assigne à chaque valeur du tuple une variable sous forme de nom
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense) #on créer (instancie) un athlète
            dic_ath[nom+" "+prenom]=athlete0 #on ajoute l'athlete à notre dico d'athlete
        for cle in dic_ath:#on parcours notre liste pour l'afficher
            print(dic_ath[cle].afficher())

    def lire_visiteur_search(self):
        b=self.connection() 
        cursor=b.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT vis_nom, vis_prenom, vis_numero FROM Visiteurs") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for ivisiteurs in resultat: #on parcours le tuple1 
            nom, prenom, numero= ivisiteurs #on assigne à chaque valeur du tuple une variable sous forme de nom
            visiteur0=Visiteur(nom,prenom,numero) #on créer (instancie) un visiteur
            dic_vis[nom+" "+prenom]=visiteur0#on ajoute l'athlete à notre dico de visiteur
        for cle in dic_vis:#on parcours notre liste pour l'afficher
            print(dic_vis[cle].afficher())
##### Programme d'éxécution #####
admin=Administrateur() #on créer un administrateur
admin.lire_athlete() #on appel la fonction
admin.lire_visiteur()
#print(dic_vis['DARDINIER Foucauld'].afficher())