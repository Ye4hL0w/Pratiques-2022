def conv_bin(n):
    assert type(n)==int
    assert n>=0
    if n==0:
        return ([0],1)
    bit=0
    tab=[]
    while n!=0:
        reste=n%2
        tab.append(reste)
        bit+=1
        n=n//2
    tab.reverse()
    return (tab,bit)
        

def tri_bulles(T):
    n = len(T)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
