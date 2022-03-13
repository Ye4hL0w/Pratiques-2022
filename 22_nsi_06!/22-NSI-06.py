def maxi(tab):
    assert type(tab)==list
    assert tab!=[]
    maxi  = tab[0]
    indice = 0
    for i in range(1,len(tab)):
        if tab[i] > maxi :
            maxi = tab[i]
            indice = i
    return (maxi,indice)

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j = j + 1
        if j == g:
            trouve = True
        i+=1
    return trouve
