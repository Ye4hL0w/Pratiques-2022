def rechercheMin(tab):
    indice_min=0
    min=tab[0]
    for i in range(1,len(tab)):
        if tab[i]<min:
            indice_min=i
            min=tab[i]
    return indice_min

def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i = i+1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j-1
    return tab
