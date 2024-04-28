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
                            ON Disciplines.ath_discipline=Disciplines.dis_id""") #on lui donne l'ordre
        resultat=cursor.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        for iathlete in resultat: #on parcours le tuple1 
            nom, prenom, naissance, pays, discipline, recompense= iathlete #on assigne à chaque valeur du tuple une variable sous forme de nom
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense) #on créer (instancie) un athlète
            dic_ath[nom+" "+prenom]=athlete0 #on ajoute l'athlete à notre dico d'athlete
        return(dic_ath)
    
    #def ad_athlete(self,nom0,prenom0,nais0,pays0,dis0,rec0):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        ordre="""INSERT INTO Athletes(ath_nom, ath_prenom, ath_naissance, ath_pays, ath_discipline, ath_recompense) 
                VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(ordre,(nom0,prenom0,nais0,pays0,dis0,rec0))
        lien.commit()#pour que la modification soit conservée

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

    def ad_athlete(self,nom0,prenom0,nais0):
        cursor=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        ordre="""INSERT INTO Athletes(ath_nom, ath_prenom, ath_naissance) 
                VALUES (%s,%s,%s)"""#on donne l'ordre
        cursor.execute(ordre,(nom0,prenom0,nais0))
        lien.commit()#pour que la modification soit conservée

    def ad_visiteur(self,nom0,prenom0):
        cursor_num=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        cursor_num.execute("""SELECT vis_numero 
                        FROM Visiteurs""") #on lui donne l'ordre
        numeros=cursor_num.fetchall() #on utilise l'attribut fetchall pour récupérer ce qu'il a lu en renvoyant un tuple1 qui contient des tuples
        #print(numeros)
        num0="A698736489"
        while num0 in numeros:
            suite0=random.choices("0123456789", k=10)
            for i in suite0:
                numf=numf+str(i)
            num0=numf

        cursor_insert=lien.cursor() #on créer un curseur où lorsque qu'on lui donnera un ordre de lecture il lira la base de donnée qu'on lui a renseigner dans lien
        ordre="""INSERT INTO Visiteurs(vis_nom, vis_prenom, vis_numero) 
                VALUES (%s,%s,%s)"""#on donne l'ordre
        cursor_insert.execute(ordre,(nom0,prenom0,num0))
        lien.commit()#pour que la modification soit conservée

    def show_athlete(self):
        admin.ecriture_athlete()
        list_SORTIE=[]
        for cle in dic_ath:
            list_SORTIE.append(dic_ath[cle].afficher())
        print(list_SORTIE)

    def show_visiteur(self):
        admin.ecriture_visiteur()
        list_SORTIE=[]
        for cle in dic_vis:
            list_SORTIE.append(dic_vis[cle].afficher())
        return(list_SORTIE)

    def search_pays(self,ENTREE):
        admin.ecriture_athlete()
        while True:
            test=False #pour ne pas afficher l'erreur le nombre de fois où le pays est différent
            for (cle,athlete) in dic_ath.items(): #on lit notre dico 
                if ENTREE==athlete.pays: 
                    infos=dic_ath[cle].afficher()
                    test=True
                    SORTIE=infos
            if test==False:
                SORTIE="Réessayer, ce pays n'est pas présent aux jeux !"
            if test==True:
                break
        return (SORTIE)

    def search_athlete(self,ENTREE):
        admin.ecriture_athlete()
        infos=dic_ath[ENTREE].afficher()
        return(infos)
            
    def search_dis(self):
        admin.ecriture_athlete()
        while True:
            valref=input("Saissisez la discipline:  ") #on demande la discipline à afficher
            test=False #pour ne pas afficher l'erreur le nombre de fois où la discipline est différente
            for (cle,athlete) in dic_ath.items(): #on lit notre dico 
                if valref==athlete.dis: 
                    infos=dic_ath[cle].afficher()
                    test=True
                    print(infos)
            if test==False:
                return("Réessayer, cette discipline n'est pas présente aux jeux !")
            if test==True:
                break

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

            
##### Programme d'éxécution #####
admin=Administrateur() #on créer un administrateur
#admin.ad_athlete()
#admin.ad_visiteur("FGHC","cvgsh")
#admin.show_athlete() #on appel la fonction
#admin.show_visiteur()
#admin.search_athlete()
#admin.search_visiteur()
#admin.search_dis()
#admin.search_pays()
lien.close()