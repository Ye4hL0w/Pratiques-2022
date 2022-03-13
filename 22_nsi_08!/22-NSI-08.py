def recherche(elt,tab):
    indice=0
    for element in tab:
        if element!=elt:
            indice+=1
        else:
            return indice
    else:
        return -1

#correction 

def recherche(elt,tab):
    resultat=-1
    for i in range(len(tab)):
        if tab[i]==elt:
            resultat=i
    return resultat


def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab)-1#-2
    while a < l[i] and i >= 0: 
      l[i+1] = l[i]
      l[i] = a
      i = i-1
    return l
