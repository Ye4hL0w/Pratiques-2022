def rechercheMinMax(tab):
    if tab==[]:
        min=None
        max=None
    else:
        min=tab[0]
        max=tab[0]
        for i in tab:
            if min>i:
                min=i
            if max<i:
                max=i
    return {'min':mini,'max':maxi}



class Carte:
    """Initialise Couleur (entre 1 Ã  4), et Valeur (entre 1 Ã  13)"""
    def __init__(self, c, v):
        assert c>0 and c<5
        assert v>0 and v<14
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10,
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for couleur in range(1,5):
            for valeur in range(1,14):
                self.contenu.append(Carte(couleur,valeur))


    """Renvoie la Carte qui se trouve Ã  la position donnÃ
©e"""
    def getCarteAt(self, pos):
        assert pos>0 and pos<=52
        return self.contenu[pos-1]