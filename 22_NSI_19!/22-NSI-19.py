def multiplication(n1,n2):
    multipli=0
    for i in range(abs(n1)):
        multipli+=n2
    if n1>0:
        return multipli
    else:
        return -multipli

def chercher(T,n,i,j):
    if i < 0 or j>=len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, m+1 , j)
    elif T[m] > n :
        return chercher(T, n, i , m-1 )
    else :
        return m
