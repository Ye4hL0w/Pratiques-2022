#Exercice 1


def delta(liste):
    assert type(liste)==liste
    if len(liste)<=1:
        return liste
    reponse=[liste[0]]
    for k in range(1,len(liste)):
        reponse.append(liste[k]-liste[k-1])
    return reponse



#Exercice 2


class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
   s = ""
   if e.gauche is not None:
       s = s + expression_infixe(e.gauche)
   s = s + str(e.valeur)
   if e.droit is not None:
       s = s + expression_infixe(e.droit)
   if e.est_une_feuille():
       return s
   return '('+ s +')'



























































