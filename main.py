from athlete import Athlete #on appel les différentes classes dans les différents modules
from visiteur import Visiteur
from pays import Pays
from mysql.connector import connect
import random
dic_ath={}
dic_vis={}

lien=connect(host="localhost",user="root", #on utilise la méthode "connect" du module "mysql.connector" pour que python se connect à notre base de donnée
                password="root",database="Olympiques")

class Administrateur:

    def ecriture_athlete(self):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        cursor.execute("""SELECT ath_nom, ath_prenom, ath_naissance, Pays.pays_nom, Disciplines.dis_nom, ath_recompense 
                        FROM Athletes 
                        INNER JOIN Pays 
                            ON Athletes.ath_pays=Pays.pays_id 
                        INNER JOIN Disciplines
                            ON Athletes.ath_discipline=Disciplines.dis_id""") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for iathlete in resultat: #on parcours le tuple1 
            nom, prenom, naissance, pays, discipline, recompense= iathlete #on assigne à chaque valeur du tuple une variable sous forme de nom
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense) #on créer (instancie) un athlète
            dic_ath[nom+" "+prenom]=athlete0 #on ajoute l'athlete à notre dico d'athlete
        return(dic_ath)

    def ecriture_visiteur(self):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée
        cursor.execute("""SELECT vis_nom, vis_prenom, vis_numero 
                          FROM Visiteurs""") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for ivisiteur in resultat: #on parcours le tuple1 
            nom, prenom, numero= ivisiteur #on assigne à chaque valeur du tuple une variable sous forme de nom
            visiteur0=Visiteur(nom,prenom,numero) #on créer (instancie) un visiteur
            dic_vis[nom+" "+prenom]=visiteur0 #on ajoute le visiteur à notre dico de visiteur
        return(dic_vis)

    def ad_athlete(self,nom0,prenom0,nais0,pays0,dis0):
#ici pour associer chaque id aux pays et à la discipline on a choisit d'utiliser un dictionnaire, cela évite les nombreuses boucle IF...ELIF...ELSE...
        id_pays={"FRANCE":"1",
               "ALGÉRIE":"2",
               "JAMAÏQUE":"3",
               "JAPON":"4",
               "CHINE":"5",}.get(pays0)
        id_dis={"JUDO":"1",
               "NATATION":"2",
               "TENNIS_DE_TABLE":"3",
               "ATHLETISME":"4",
               "GYMNASTIQUE_ARTISTIQUE":"5",}.get(dis0)
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        ordre="""INSERT INTO Athletes(ath_nom, ath_prenom, ath_naissance, ath_pays, ath_discipline) 
                VALUES (%s,%s,%s,%s,%s)"""#on donne l'ordre
        cursor.execute(ordre,(nom0,prenom0,nais0,id_pays,id_dis))
        lien.commit()#pour que la modification soit conservée

    def ad_visiteur(self,nom0,prenom0):
        suite0=random.choices("0123456789", k=10) #on prend une sequence de 10 chiffres dans une liste
        numf=""
        for i in suite0:
            numf=numf+str(i)#on créer une seule et unique chaine de caractère de cette séquence
        num0=numf

        cursor_insert=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        ordre="""INSERT INTO Visiteurs(vis_nom, vis_prenom, vis_numero) 
                VALUES (%s,%s,%s)"""#on donne l'ordre
        cursor_insert.execute(ordre,(nom0,prenom0,num0))
        lien.commit()#pour que la modification soit conservée

    def del_athlete(self,nom0,prenom0):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        ordre="""DELETE FROM Athletes 
                WHERE ath_nom=%s AND ath_prenom=%s"""#on donne l'ordre
        cursor.execute(ordre,(nom0,prenom0))
        lien.commit()#pour que la modification soit conservée

    def del_visiteur(self,nom0,prenom0):
        ENTREE=nom0+" "+prenom0
        dic_vis=admin.ecriture_visiteur()
        if ENTREE in dic_vis.keys():
            cursor_insert=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
            ordre="""DELETE FROM Visiteurs 
                    WHERE vis_nom=%s AND vis_prenom=%s""" #on donne l'ordre
            cursor_insert.execute(ordre,(nom0,prenom0))
            lien.commit()#pour que la modification soit conservée
        else:
            return("ERREUR")

    def show_athlete(self):
        dic_ath=admin.ecriture_athlete()
        liste_SORTIE=[] #on est obligé de mettre tous les infos (une liste) de chaque athlète dans une liste pour seulement à faire un for element dans notre I.G
        for cle in dic_ath:
            athlete_infos=dic_ath[cle].afficher()
            liste_SORTIE.append(athlete_infos)
        return(liste_SORTIE)

    def show_visiteur(self):
        dic_vis=admin.ecriture_visiteur()
        list_SORTIE=[] #on est obligé de mettre tous les infos (une liste) de chaque visiteur dans une liste pour seulement à faire un for element dans notre I.G
        for cle in dic_vis:
            visiteur_infos=dic_vis[cle].afficher()
            list_SORTIE.append(visiteur_infos)
        return(list_SORTIE)

    def search_athlete(self,ENTREE):
        dic_ath=admin.ecriture_athlete()
        if ENTREE in dic_ath.keys(): #on test si l'athlète rentrée par l'utilisateur est dans notre dico
            infos=dic_ath[ENTREE].afficher()
            return(infos)
        else:
            return ("ERREUR")

    def search_pays(self,ENTREE):
        dic_ath=admin.ecriture_athlete()
        liste_pays=[]
        liste_SORTIE=[] #on est obligé de mettre tous les infos (une liste) de chaque athlète dans une liste pour seulement à faire un for element dans notre I.G
        for (cle,athlete) in dic_ath.items(): #on lit notre dico pour ajouter tous les pays dans la liste_pays
            liste_pays.append(athlete.pays)
        if ENTREE in liste_pays: #on vérifie bien que le pays entrée par l'utilisateur figure dans la liste
            for (cle,athlete) in dic_ath.items(): #et on re-parcours le dico pour afficher les infos de chaque athlete appartenant au pays rentré par l'utilisateur 
                if ENTREE==athlete.pays: 
                    athlete_infos=dic_ath[cle].afficher()
                    liste_SORTIE.append(athlete_infos)
            return(liste_SORTIE)
        else:
            return("ERREUR")
        
    def search_dis(self,ENTREE):
        dic_ath=admin.ecriture_athlete()
        liste_dis=[]
        liste_SORTIE=[] #on est obligé de mettre tous les infos (une liste) de chaque athlète dans une liste pour seulement à faire un for element dans notre I.G
        for (cle,athlete) in dic_ath.items(): #on lit notre dico pour ajouter tous les pays dans la liste_pays
            liste_dis.append(athlete.dis)
        if ENTREE in liste_dis: #on vérifie bien que le pays entrée par l'utilisateur figure dans la liste
            for (cle,athlete) in dic_ath.items(): #et on re-parcours le dico pour afficher les infos de chaque athlete appartenant au pays rentré par l'utilisateur 
                if ENTREE==athlete.dis: 
                    athlete_infos=dic_ath[cle].afficher()
                    liste_SORTIE.append(athlete_infos)
            return(liste_SORTIE)
        else:
            return("ERREUR")
        
    def search_visiteur_nom(self,ENTREE):
        dic_vis=admin.ecriture_visiteur()
        if ENTREE in dic_vis.keys(): #on test si l'athlète rentrée par l'utilisateur est dans notre dico
            infos=dic_vis[ENTREE].afficher()
            return(infos)
        else:
            return ("ERREUR")

    def search_visiteur_num(self,ENTREE):
        dic_vis=admin.ecriture_visiteur()
        liste_num=[]
        for (cle,athlete) in dic_vis.items(): #on lit notre dico pour ajouter tous les numeros dans la liste_num
            liste_num.append(athlete.numero)
        if ENTREE in liste_num: #on vérifie bien que le pays entrée par l'utilisateur figure dans la liste
            for (cle,visiteur) in dic_vis.items(): #et on re-parcours le dico pour afficher les infos du visiteur aillant le m^me numéro que celui rentré par l'utilisateur 
                if ENTREE==visiteur.numero: 
                    visiteur_infos=dic_vis[cle].afficher()
            return(visiteur_infos)
        else:
            return("ERREUR")
            
##### Programme d'éxécution #####

admin=Administrateur() #on créer un administrateur
#admin.ad_athlete("Darius","TOP","1955-06-19","FRANCE","JUDO")
#admin.ad_visiteur("DEBERGNE","Dylan")
#admin.del_visiteur("DEBEGNE","Dylan")
#admin.del_athlete("DARIUS","TOP")
#admin.show_athlete()
#admin.show_visiteur()
#admin.search_athlete("RINER Teddy")
#admin.search_visiteur_num("1698736489")
#admin.search_dis("JUDO")
#admin.search_pays("FRANCE")

