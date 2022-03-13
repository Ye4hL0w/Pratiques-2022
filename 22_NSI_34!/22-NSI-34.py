
def occurence_max(chaine):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    occurence=[0]*26
    for caractere in chaine:
        if caractere in alphabet:
            i=0
            while alphabet[i]!=caractere:
                i+=1
            occurence[i]+=1
    indice_plus_grand=0
    for indice in rannge(len(occurence)):
        if occurence[indice]>occurence[indice_plus_grand]:
            indice_plus_grand=indice
    return alphabet[indice_plus_grand]
        
        
        
        
    


def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] 
# on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(len(image[0]):
            L[i][j] = 255-image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inferieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(len(image):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
