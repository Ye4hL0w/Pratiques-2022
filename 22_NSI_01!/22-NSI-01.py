#Exercice 1


def recherchce(caractere,mot):
    compteur=0
    for lettre in mot:
        if lettre==caractere:
            compteur+=1
    return compteur



#Exercice 2


Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
        if arendre == 0:
            return solution
        p = pieces[i]
        if p <= arendre :
            solution.append(p)
            return rendu_glouton(arendre - p, solution, i)
        else :
            return rendu_glouton(arendre, solution, i+1)
