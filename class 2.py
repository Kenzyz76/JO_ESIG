class Visiteurs :
    def __init__(self, nom0, prenom0, numero_billet):
        self.nom = nom0
        self.prenom = prenom0
        self.billet = numero_billet

    def afficher (self):
        liste=[self.nom, self.prenom, self.billet]
        return liste
    
    
    

        
