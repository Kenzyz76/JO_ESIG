from athlete import Athlete #on appel les différentes classes dans les différents modules
from visiteur import Visiteur
from pays import Pays
from mysql.connector import connect
dic_ath={}
dic_vis={}

lien=connect(host="localhost",user="root", #on utilise la méthode "connect" du module "mysql.connector" pour que python se connect à notre base de donnée
                password="Akenzi06",database="Olympiques")

class Administrateur:

    def ecriture_athlete(self):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT ath_nom, ath_prenom, ath_naissance, Pays.pays_nom, Disciplines.dis_nom, ath_recompense FROM Athletes INNER JOIN Pays ON Athletes.ath_pays=Pays.pays_id INNER JOIN Disciplines ON ath_discipline=dis_id") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for iathlete in resultat: #on parcours le tuple1 
            nom, prenom, naissance, pays, discipline, recompense= iathlete #on assigne à chaque valeur du tuple une variable sous forme de nom
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense) #on créer (instancie) un athlète
            dic_ath[nom+" "+prenom]=athlete0 #on ajoute l'athlete à notre dico d'athlete
        return(dic_ath)

    def afficher_athlete(self):
        admin.ecriture_athlete()
        for cle in dic_ath: #on parcours notre dico pour l'afficher
            return dic_ath[cle].afficher()

    def search_athlete(self):
        admin.ecriture_athlete()
        while True:
            cle=input("Saissisez:NOM Prénom  ") #on demande le nom et prenom du visiteur à afficher
            if cle not in dic_ath.keys(): #on test si cette personne existe dans notre dico visiteur
                print("Réessayer, cette personne n'est pas renseignée !")
            else:
                infos=dic_ath[cle].afficher()
                print(infos)
                break

    def search_dis(self):
        admin.ecriture_athlete()
        while True:
            valref=input("Saissisez la discipline:  ") #on demande la discipline à afficher
            test=False #pour ne pas afficher l'erreur le nombre de fois où la discipline est différente
            for (cle,athlete) in dic_ath.items(): #on lit notre dico 
                if valref==athlete.dis: 
                    infos=dic_ath[cle].afficher()
                    print(infos)
                    test=True
            if test==False:
                print("Réessayer, cette discipline n'est pas présente aux jeux !")
            if test==True:
                break
                
    def search_pays(self):
        admin.ecriture_athlete()
        while True:
            valref=input("Saissisez le pays:  ") #on demande le pays à afficher
            test=False #pour ne pas afficher l'erreur le nombre de fois où le pays est différent
            for (cle,athlete) in dic_ath.items(): #on lit notre dico 
                if valref==athlete.pays: 
                    infos=dic_ath[cle].afficher()
                    print(infos)
                    test=True
            if test==False:
                print("Réessayer, ce pays n'est pas présent aux jeux !")
            if test==True:
                break

    def ecriture_visiteur(self):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("SELECT vis_nom, vis_prenom, vis_numero FROM Visiteurs") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for ivisiteur in resultat: #on parcours le tuple1 
            nom, prenom, numero= ivisiteur #on assigne à chaque valeur du tuple une variable sous forme de nom
            visiteur0=Visiteur(nom,prenom,numero) #on créer (instancie) un visiteur
            dic_vis[nom+" "+prenom]=visiteur0 #on ajoute le visiteur à notre dico de visiteur
        return(dic_vis)

    def afficher_visiteur(self):
        admin.ecriture_visiteur()
        for cle in dic_vis:#on parcours notre dico pour l'afficher
            return dic_vis[cle].afficher()

    def search_visiteur(self):
        admin.ecriture_visiteur()
        while True:
            cle=input("Saissisez votre:NOM Prénom  ") #on demande le nom et prenom du visiteur à afficher
            if cle not in dic_vis.keys(): #on test si cette personne existe dans notre dico visiteur
                print("Réessayer, cette personne n'est pas renseignée !")
            else:
                infos=dic_vis[cle].afficher()
                print(infos)
                break
            
    #def ad_athlete(self):
       #ordre="INSERT INTO Athletes(ath_nom, ath_prenom, ath_naissance, ath_pays, ath_discipline, ath_recompense) VALUES (%s,%s,%s,%s,%s,%s)"
       #cursor.execute(ordre,)

##### Programme d'éxécution #####
admin=Administrateur() #on créer un administrateur
print(admin.afficher_athlete()) #on appel la fonction
#admin.afficher_visiteur()
#admin.search_athlete()
#admin.search_visiteur()
#admin.search_dis()
#admin.search_pays()