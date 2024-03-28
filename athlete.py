from datetime import datetime
class Athlete:
    def __init__(self,nom0,prenom0,nais0,pays0,dis0,rec0):
        self.nom=nom0
        self.prenom=prenom0
        self.nais=nais0
        self.pays=pays0
        self.dis=dis0
        self.rec=rec0

    def afficher(self):
        p=self.nais.strftime("%d/%m/%Y")
        liste=[self.nom,self.prenom,self.pays,p,self.dis,self.rec]
        return (liste)
    
    def ajouter_rec(self):
        if self.rec==None:
            m=input("Quelle récompense a-t-il obtenu ?")
            self.rec=m

        if self.rec!=None:
            print("Erreur, l'athlète possède déjà une récompense !")
            return False
            
        
    
