class Athlètes:
    def __init__(self,nom0,prenom0,nais0,pays0,dis0,rec0):
        self.nom=nom0
        self.prenom=prenom0
        self.nais=nais0
        self.pays=pays0
        self.dis=dis0
        self.rec=rec0

    def afficher_all(self):
        liste=[self.nom,self.prenom,self.nais,self.pays,self.dis,self.rec]
        return (liste)
    
    def ajouter_rec(self):
        if self.rec==None:
            m=input("Quelle récompense a-t-il obtenu ?")
            self.rec=m

        if self.rec!=None:
            return False
            print("Erreur, l'athlète possède déjà une récompense !")   
        

class Pays:
    def __init__(self,nom0,continent0):
        self.nom=nom0
        self.continent=continent0

    def afficher (self):
        return ([self.nom,self.continent])
    
        
