def multiplication(n1,n2):
    multipli=0
    for i in range(abs(n1)):
        multipli+=n2
    if n1>0:
        return multipli
    else: 
        return -multipli

def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m-1	
    return False
