
def selection_enclos(table_animaux,num_enclos):
    sortie=[]
    for animal in table_animaux:
        if animal["enclos"]==num_enclos:
            sortie.append(animal)
    return sortie

animaux = [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g)// 3 -1
        indice = g + 3 * (nombre_de_triplets // 2)
        print("indice vaut",indice)
        if tab[indice]==tab[indice+1] : #pas intrus
            return trouver_intrus(tab,indice+3,d)
        else:
            return trouver_intrus(tab,g,indice)