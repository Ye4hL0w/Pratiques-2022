
def verifie(tab):
    for indice in range(1,len(tab)-1):
        if tab[indice]>tab[indice+1]:
            return False
    return True

urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin]=1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


