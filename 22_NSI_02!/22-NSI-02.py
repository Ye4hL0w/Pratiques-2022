#Exercice 1

def moyenne(liste):
    assert type(liste)==list
    numerateur=0
    denominateur=0
    for tupleuh in liste:
        numerateur+=tupleuh[0]*tupleuh[1]
        denominateur+=tupleuh[1]
    return numerateur/denominateur



#Exercice 2


def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
