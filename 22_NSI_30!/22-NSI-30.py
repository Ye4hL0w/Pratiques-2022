
def fusion(tab1,tab2):
    final=[]
    curseur1=0
    curseur2=0
    while curseur1<len(tab1) and curseur2<len(tab2):
        if tab1[curseur1]<tab2[curseur2]:
            final.append(tab1[curseur1])
            curseur1+=1
        else:
            final.append(tab2[curseur2])
            curseur2+=1
    if curseur1==len(tab1):#il reste des elements de table 2 a mettre
        while curseur1<len(tab2):
            final.append(tab2[curseur2])
            curseur2+=1
    else:
        while curseur1<len(tab1):
            final.append(tab1[curseur1])
            curseur1+=1
    return final
            

def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(nombre) == 1:
        return dico[nombre]

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
		 ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]
    
        
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + rom_to_dec(nombre_droite)
        else:
            return rom_to_dec(nombre_droite) - dico[nombre[0]]

assert rom_to_dec("CXLII") == 142
