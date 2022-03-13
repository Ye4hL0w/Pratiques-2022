#Exercice 1
def recherche(tab,n):
    if tab[0]==n:
        return 0
    if tab[-1]==n:
        return len(tab)-1
    indice_debut=0
    indice_fin=len(tab)-1
    while abs(indice_debut-indice_fin)>1:
        indice_milieu=(indice_debut+indice_fin)//2
        if tab[indice_milieu]==n:
            return indice_milieu
        elif n<tab[indice_milieu]:
            indice_fin=indice_milieu
        else:
            indice_debut=indice_milieu
        return -1
    

#Exercice 2

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre)+decalage)%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat
