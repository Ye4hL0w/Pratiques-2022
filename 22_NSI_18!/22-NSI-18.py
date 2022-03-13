t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve,date):
    assert type(releve)==list
    assert type(date)==list
    assert len(date)==len(releve)
    indice_minimum=0
    for indice in range(1,len(releve)):
        if releve[indice]<releve[indice_minimun]:
            indice_minimum=indice
    return(releve[indice_minimum],date[indice_minimum])

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
        result = caractere+result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine==inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)