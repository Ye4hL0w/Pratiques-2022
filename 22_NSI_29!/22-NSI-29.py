
def fibonacci(n):
    if n==1 or n==2:
        return 1
    u_n_moins_un=1
    u_n=1
    for i in range (3,n+1):
        tempo=u_n
        u_n+=u_n_moins_un
        u_n_moins_un=tempo

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi =  []
    
    for compteur in range(len(liste_eleves)):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]
            
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)