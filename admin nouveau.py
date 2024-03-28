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

    def lecture_athlete(self):
        b=self.connection() 
        cursor=b.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT ath_nom, ath_prenom, ath_naissance, Pays.pays_nom, ath_discipline, ath_recompense FROM Athletes INNER JOIN Pays ON Athletes.ath_pays=Pays.pays_id") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        return (resultat)

    def ecriture_athlete(self):
        resultat=admin.lecture_athlete()
        for iathlete in resultat: #on parcours le tuple1 
            nom, prenom, naissance, pays, discipline, recompense= iathlete #on assigne à chaque valeur du tuple une variable sous forme de nom
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense) #on créer (instancie) un athlète
            dic_ath[nom+" "+prenom]=athlete0 #on ajoute l'athlete à notre dico d'athlete
        return(dic_ath)

    def afficher_athlete(self):
        resultat=admin.lecture_athlete()
        admin.ecriture_athlete()
        for cle in dic_ath: #on parcours notre liste pour l'afficher
            print(dic_ath[cle].afficher())

    def search_athlete(self):
        resultat=admin.lecture_athlete()
        admin.ecriture_athlete()
        while True:
            cle=input("Saissisez:NOM Prénom") #on demande le nom et prenom du visiteur à afficher
            if cle not in dic_ath.keys():
                print("Réessayer, cette personne n'est pas renseignée !")
            else:
                infos=dic_ath[cle].afficher()
                print(infos)
                break

    def lecture_visiteur(self):
        b=self.connection() 
        cursor=b.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT vis_nom, vis_prenom, vis_numero FROM Visiteurs") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        return (resultat)

    def ecriture_visiteur(self):
        resultat=admin.lecture_visiteur()
        for ivisiteur in resultat: #on parcours le tuple1 
            nom, prenom, numero= ivisiteur #on assigne à chaque valeur du tuple une variable sous forme de nom
            visiteur0=Visiteur(nom,prenom,numero) #on créer (instancie) un visiteur
            dic_vis[nom+" "+prenom]=visiteur0 #on ajoute le visiteur à notre dico de visiteur
        return(dic_vis)

    def afficher_visiteur(self):
        resultat=admin.lecture_visiteur()
        admin.ecriture_visiteur()
        for cle in dic_vis:#on parcours notre liste pour l'afficher
            print(dic_vis[cle].afficher())

    def search_visiteur(self):
        resultat=admin.lecture_visiteur()
        admin.ecriture_visiteur()
        while True:
            cle=input("Saissisez votre:NOM Prénom") #on demande le nom et prenom du visiteur à afficher
            if cle not in dic_vis.keys():
                print("Réessayer, cette personne n'est pas renseignée !")
            else:
                infos=dic_vis[cle].afficher()
                print(infos)
                break
            
    
##### Programme d'éxécution #####
admin=Administrateur() #on créer un administrateur
#admin.afficher_athlete() #on appel la fonction
#admin.afficher_visiteur()
#admin.search_athlete()
admin.search_visiteur()