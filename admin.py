from athlete import Athlete
from visiteur import Visiteur
from pays import Pays
from mysql.connector import connect
liste0=[]
class Administrateur:
    def connection():
        bdd=connect(host="localhost",user="root",
                    password="root",database="Olympiques")
        return(bdd)

def lire_athlete(self):
        bdd=self.connection()
        cursor=bdd.cursor()
        cursor.execute("SELECT ath_nom, ath_prenom, ath_naissance, act_pays, act_discipline, act_recompense FROM Athletes")
        resultat=cursor.fetchall()
        for iathlete in resultat:
            nom, prenom, naissance, pays, discipline, recompense= iathlete
            athlete0=Athlete(nom,prenom,naissance,pays,discipline, recompense)
            liste0.append(athlete0)
        return(liste0)