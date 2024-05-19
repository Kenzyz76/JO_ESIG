class Visiteur :
    def __init__(self, nom0, prenom0, numero0):#on définit les attributs de la classe
        self.nom = nom0 
        self.prenom = prenom0
        self.numero = numero0

    def listing(self):
        liste=[self.nom, self.prenom, self.numero]
        return liste
    
    
    

        
