#Exercice 1
def correspond(mot,mot_a_trous):
    assert type(mot)==str
    assert type(mot_a_trous)==str
    if len(mot)!=len(mot_a_trous):
        return False
    for indice in range(len(mot_a_trous)):
        if mot_a_trous[indice]!="*":
            if mot_a_trous[indice]!=mot[indice]:
                return False
    return True
        
     
#Exercice 2
def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(plan)
    for i in range(N-1):
        if plan[personne] == "A":
            return False
        else:
            personne = plan[personne]
    return True