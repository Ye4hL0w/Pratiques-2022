def maxi(tab):
    indice_max=0
    for indice in range(1,len(tab)):
        if tab[indice]>tab[indice_max]:
            indice_max=indice
    return (tab[indice_max],indice_max)
    
def positif(T):
    T2 = liste(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

