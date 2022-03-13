#Exercice 1
def moyenne(tab):
    assert type(tab)==list
    if tab==[]:
        return "erreur"
    somme=0
    for nombre in tab:
        somme+=nombre
    return somme/len(tab)


#Exercice 2
def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i= tab[0]
    j= (tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j-1
    return tab