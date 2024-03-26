from athlete import Athlete
from visiteur import Visiteur
from pays import Pays
from mysql.connector import connect
liste0=[]
class Administrateur:
    def connection(self):
        bdd=connect(host="localhost",user="root",
                    password="root",database="Olympiques")
        return(bdd)

    def lire_athlete(self):
        bdd=self.connection()
        cursor=bdd.cursor()
        cursor.execute("SELECT ath_nom, ath_prenom, ath_naissance, Pays.pays_nom, ath_discipline, ath_recompense FROM Athletes INNER JOIN Pays ON Athletes.ath_pays=Pays.pays_id")
        resultat=cursor.fetchall()
        for iathlete in resultat:
            nom, prenom, naissance, pays, discipline, recompense= iathlete
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense)
            liste0.append(athlete0)
        for element in liste0:
            print(element.afficher_all())

admin=Administrateur()
admin.lire_athlete()