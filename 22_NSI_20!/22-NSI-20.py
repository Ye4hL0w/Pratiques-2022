a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

def xorBac(tab1,tab2):
    assert type(tab1)==list
    assert type(tab2)==list
    assert len(tab1)==len(tab2)
    resulat=[]
    for i in range(len(tab1)):
        somme=tab1[i]+tab2[i]
        if somme==0 or somme==2:
            resultat.append(0)
        else:
            resultat.apppend(1)
    return resultat

def xorMieux(tab1,tab2):
    assert type(tab1)==list
    assert type(tab2)==list
    assert len(tab1)==len(tab2)
    resulat=[]
    for i in range(len(tab1)):
        resultat.append(1 if tab[i]!=tab2[i] else 0)
    return resultat

def xorGenial(tab1,tab2):
    return [1 if tab1[1]!=tab2[i] else 0 for i in range(len(tab1))]

class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau
    
    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])
    
    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])
    
    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)
        
    #test de la somme de chaque ligne
    for i in range(0, n):
        if carre.somme_ligne(i) != s:
            return False
        
    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col(j) != s:
            return False
         
    #test de la somme de chaque diagonale
    if sum([carre.valeurs[k][k] for k in range(n)]) != s:
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
    
    return s


