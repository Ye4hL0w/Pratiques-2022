def taille(arbre,lettre):
    resultat=0
    if arbre[lettre][0]!="": #ya un enfant à gauche
        resultat+=taille(arbre,arbre[lettre][0])
    if arbre[lettre][1]!="": #ya un enfant à droite
        resultat+=taille(arbre,arbre[lettre][1])
    return 1+resultat

def tri_iteratif(tab):
    for k in range( len(tab) , 0, -1):
        imax = 0
        for i in range(0 , k ):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab
