#Exercice 1
def rendu(somme_a_rendre):
    n1 = somme_a_rendre//5
    somme_a_rendre-=n1*5
    n2 = somme_a_rendre//2
    somme_a_rendre-=n2*2
    n3 = somme_a_rendre
    return [n1,n2,n3]
    
def rendu_court(somme_a_rendre):
    return [somme_a_rendre//5,(somme_a_rendre%5)//2,(somme_a_rendre%5)%2]
    
#Exercice 2
class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element) 
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None:
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None 
