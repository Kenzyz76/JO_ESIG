class Pays:
    def __init__(self,nom0,continent0):
        self.nom=nom0
        self.continent=continent0

    def afficher (self):
        return ([self.nom,self.continent])