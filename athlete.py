from datetime import datetime
class Athlete:
    def __init__(self,nom0,prenom0,nais0,pays0,dis0,rec0):#on définit les attributs de la classe
        self.nom=nom0
        self.prenom=prenom0
        self.nais=nais0
        self.pays=pays0
        self.dis=dis0
        self.rec=rec0

    def listing(self):
        date=self.nais.strftime("%d/%m/%Y")
        liste=[self.nom,self.prenom,self.pays,date,self.dis,self.rec]
        return (liste)

            
        
    
